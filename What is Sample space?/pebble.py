import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
import math
import random

class SampleSpace:
    def __init__(self, outcomes):
        total = sum(outcomes.values())
        if abs(total - 1.0) > 1e-9:
            raise ValueError("Probabilities must sum to 1.")
        self.outcomes = outcomes

    def probability(self, event):
        return sum(self.outcomes[o] for o in event)
    
    def visualize(
        self,
        title="pebble world",
        *,
        cmap_name="turbo",
        palette=None,
        background_color="#000000",
        panel_color="#0b0b10",
        text_color="#f9fafb",
        outline_color="#2a2f3a",
        label_box_color="#111827",
        pebble_edge_color="#ffffff",
        show_sparkles=True,
        sparkle_count=70,
        min_pebble_size=350,
        max_pebble_size=2600,
        show_probs=True,
    ):
        labels = list(self.outcomes.keys())
        probs = list(self.outcomes.values())

        plt.style.use("seaborn-v0_8")

        fig, ax = plt.subplots(figsize=(10, 3.8))
        fig.patch.set_facecolor(background_color)
        ax.set_facecolor(panel_color)

        n = len(labels)
        xs = list(range(n))

        # Slight arc/jitter so it doesn't look like a flat line of dots.
        if n == 1:
            ys = [0.0]
        else:
            center = (n - 1) / 2
            base_arc = [0.14 * math.cos((i - center) * math.pi / max(n - 1, 1)) for i in range(n)]
            mean_p = 1.0 / n
            prob_bump = [0.25 * (p - mean_p) for p in probs]
            ys = [base_arc[i] + prob_bump[i] - 0.05 for i in range(n)]

        # Scale pebble area by probability, with guardrails so small probs are still visible.
        if n == 0:
            raise ValueError("No outcomes to visualize.")
        p_min, p_max = min(probs), max(probs)
        if abs(p_max - p_min) < 1e-12:
            sizes = [0.5 * (min_pebble_size + max_pebble_size)] * n
        else:
            sizes = [
                min_pebble_size
                + (p - p_min) * (max_pebble_size - min_pebble_size) / (p_max - p_min)
                for p in probs
            ]

        if palette is None:
            try:
                cmap = mpl.colormaps.get_cmap(cmap_name)
                if hasattr(cmap, "resampled"):
                    cmap = cmap.resampled(max(n, 1))
            except Exception:
                # Older Matplotlib fallback
                cmap = cm.get_cmap(cmap_name, max(n, 1))

            if n == 1:
                colors = [cmap(0.5)]
            else:
                colors = [cmap(i / (n - 1)) for i in range(n)]
        else:
            # palette can be a list (cycled) or a dict mapping labels -> color
            if isinstance(palette, dict):
                colors = [palette.get(label, "#4c78a8") for label in labels]
            else:
                palette_list = list(palette)
                if len(palette_list) == 0:
                    raise ValueError("palette must be a non-empty list/tuple or a dict")
                colors = [palette_list[i % len(palette_list)] for i in range(n)]

        # View bounds (used for background extent)
        x_min, x_max = -0.8, n - 0.2
        y_min, y_max = -1.0, 1.0

        # Subtle background gradient (still a black theme, but less flat)
        h, w = 220, 900
        grad = []
        for yy in range(h):
            row = []
            v = yy / (h - 1)
            for xx in range(w):
                u = xx / (w - 1)
                # Two soft blobs + a gentle vignette
                d1 = (u - 0.25) ** 2 + (v - 0.30) ** 2
                d2 = (u - 0.78) ** 2 + (v - 0.65) ** 2
                blob = 0.55 * math.exp(-d1 / 0.030) + 0.35 * math.exp(-d2 / 0.020)
                vignette = 1.0 - 0.9 * ((u - 0.5) ** 2 + (v - 0.5) ** 2)
                row.append(max(0.0, min(1.0, 0.06 + 0.10 * blob + 0.04 * vignette)))
            grad.append(row)

        ax.imshow(
            grad,
            extent=[x_min, x_max, y_min, y_max],
            origin="lower",
            cmap="magma",
            alpha=0.35,
            zorder=0,
            aspect="auto",
        )

        # Optional sparkles (kept subtle)
        if show_sparkles and sparkle_count > 0:
            rng = random.Random((hash(tuple(labels)) ^ hash(title)) & 0xFFFFFFFF)
            sx = [rng.uniform(x_min, x_max) for _ in range(sparkle_count)]
            sy = [rng.uniform(-0.65, 0.85) for _ in range(sparkle_count)]
            ss = [rng.uniform(4, 18) for _ in range(sparkle_count)]
            ax.scatter(
                sx,
                sy,
                s=ss,
                c="white",
                alpha=0.10,
                linewidths=0,
                zorder=1,
            )

        # Drop shadow (offset slightly)
        ax.scatter(
            [x + 0.05 for x in xs],
            [y - 0.06 for y in ys],
            s=[s * 1.02 for s in sizes],
            c="black",
            alpha=0.35,
            linewidths=0,
            zorder=2,
        )

        # Multi-layer glow
        for scale, alpha in ((1.90, 0.10), (1.55, 0.14), (1.25, 0.18)):
            ax.scatter(
                xs,
                ys,
                s=[s * scale for s in sizes],
                c=colors,
                alpha=alpha,
                linewidths=0,
                zorder=3,
            )

        # Main pebbles
        ax.scatter(
            xs,
            ys,
            s=sizes,
            c=colors,
            alpha=0.97,
            linewidths=1.6,
            edgecolors=pebble_edge_color,
            zorder=4,
        )

        # Specular highlight (small, offset)
        ax.scatter(
            [x - 0.06 for x in xs],
            [y + 0.06 for y in ys],
            s=[max(18, s * 0.14) for s in sizes],
            c="white",
            alpha=0.20,
            linewidths=0,
            zorder=5,
        )

        # Labels under each pebble.
        for i, label in enumerate(labels):
            prob_text = f"\n{probs[i]:.2f}" if show_probs else ""
            ax.annotate(
                f"{label}{prob_text}",
                (xs[i], ys[i]),
                xytext=(0, -44),
                textcoords="offset points",
                ha="center",
                va="top",
                fontsize=10,
                color=text_color,
                bbox=dict(
                    boxstyle="round,pad=0.35",
                    facecolor=label_box_color,
                    edgecolor=outline_color,
                    linewidth=1.2,
                ),
                zorder=4,
            )

        ax.set_title(title, fontsize=18, fontweight="bold", pad=16, color=text_color)

        # Clean layout: no axes, subtle baseline for grounding.
        ax.axhline(-0.05, color=outline_color, linewidth=1.2, alpha=0.9, zorder=1)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.axis("off")

        fig.tight_layout()
        plt.show()

def uniform_sample_space(outcomes):
    n = len(outcomes)
    prob = 1.0 / n
    return SampleSpace({o: prob for o in outcomes})


if __name__ == "__main__":
    # Example usage so running `python .\pebble.py` shows something.
    space = SampleSpace({"red": 0.5, "blue": 0.3, "green": 0.2})
    space.visualize("Pebble world")
