import math
import random

import matplotlib.pyplot as plt


class NaiveSampleSpace():
    def __init__(self, outcomes):
        """
        outcomes: a list of possible outcomes
        example: ['H', 'T'] for a coin flip
        example: [1, 2, 3, 4, 5, 6] for a die roll
       
        """
        self.outcomes = list(outcomes)
        self.n = len(outcomes)

        if self.n == 0:
            raise ValueError ("Sample space must have at least one outcome.")
        

    def probability(self, event):
        """
        event: set of possible outcomes

        
        """
        favourable_outcomes = 0
        for outcome in event:
            if outcome in self.outcomes:
                favourable_outcomes += 1

        return favourable_outcomes / self.n
        
    def support(self):
        """
        returns the list of all possible outcomes
        """
        return self.outcomes
    

class NaiveSampleSpaceVisual(NaiveSampleSpace):
    def visualize(
        self,
        event=None,
        title="naive probability visualization",
        *,
        background_color="#000000",
        panel_color="#0b0b10",
        text_color="#f9fafb",
        outline_color="#2a2f3a",
        event_color="#e11d48",
        non_event_color="#10b981",
        show_sparkles=True,
        sparkle_count=60,
        min_size=1300,
        max_size=2600,
        show_probs=True,
    ):
        labels = list(self.outcomes)
        n = len(labels)
        if n == 0:
            raise ValueError("No outcomes to visualize.")

        event_set = set(event) if event is not None else set()
        probs = [1.0 / n] * n

        plt.style.use("seaborn-v0_8")
        fig, ax = plt.subplots(figsize=(10, 3.8))
        fig.patch.set_facecolor(background_color)
        ax.set_facecolor(panel_color)

        xs = list(range(n))
        if n == 1:
            ys = [0.0]
        else:
            center = (n - 1) / 2
            ys = [0.12 * math.cos((i - center) * math.pi / max(n - 1, 1)) - 0.03 for i in range(n)]

        # Size pebbles (uniform sample space, but still add depth + emphasis).
        if n == 1:
            sizes = [max_size]
        else:
            sizes = [0.75 * max_size for _ in range(n)]
        sizes = [max(min_size, s) for s in sizes]

        colors = [event_color if (event is not None and label in event_set) else non_event_color for label in labels]

        x_min, x_max = -0.8, n - 0.2
        y_min, y_max = -1.0, 1.0

        # Custom background (distinct from pebble world): aurora waves + scanlines + vignette.
        # Uses an RGB image (not a colormap) to keep the look unique.
        h, w = 240, 900
        try:
            import numpy as np

            yy = np.linspace(0.0, 1.0, h)[:, None]
            xx = np.linspace(0.0, 1.0, w)[None, :]

            vignette = 1.0 - 1.15 * ((xx - 0.5) ** 2 + (yy - 0.5) ** 2)
            vignette = np.clip(vignette, 0.0, 1.0)

            waves = (
                0.55 * np.sin(2 * math.pi * (1.25 * xx + 0.35 * yy))
                + 0.35 * np.sin(2 * math.pi * (0.65 * xx - 1.10 * yy))
                + 0.20 * np.sin(2 * math.pi * (2.10 * xx + 1.80 * yy))
            )
            waves = (waves + 1.0) / 2.0

            scan = 0.5 + 0.5 * np.sin(2 * math.pi * (yy * 42.0))
            scan = 0.06 * scan

            base = 0.03 + 0.10 * waves * vignette + scan
            base = np.clip(base, 0.0, 1.0)

            # Colorize: deep navy -> neon-teal -> purple aurora.
            r = np.clip(0.05 + 0.45 * (base ** 1.8), 0.0, 1.0)
            g = np.clip(0.06 + 0.75 * (base ** 1.2), 0.0, 1.0)
            b = np.clip(0.10 + 0.95 * (base ** 1.0), 0.0, 1.0)
            bg = np.dstack([r, g, b])
        except Exception:
            bg = []
            for yy in range(h):
                row = []
                v = yy / (h - 1)
                scan = 0.06 * (0.5 + 0.5 * math.sin(2 * math.pi * (v * 42.0)))
                for xx in range(w):
                    u = xx / (w - 1)
                    vignette = 1.0 - 1.15 * ((u - 0.5) ** 2 + (v - 0.5) ** 2)
                    vignette = max(0.0, min(1.0, vignette))
                    waves = (
                        0.55 * math.sin(2 * math.pi * (1.25 * u + 0.35 * v))
                        + 0.35 * math.sin(2 * math.pi * (0.65 * u - 1.10 * v))
                        + 0.20 * math.sin(2 * math.pi * (2.10 * u + 1.80 * v))
                    )
                    waves = (waves + 1.0) / 2.0
                    base = max(0.0, min(1.0, 0.03 + 0.10 * waves * vignette + scan))
                    r = max(0.0, min(1.0, 0.05 + 0.45 * (base ** 1.8)))
                    g = max(0.0, min(1.0, 0.06 + 0.75 * (base ** 1.2)))
                    b = max(0.0, min(1.0, 0.10 + 0.95 * (base ** 1.0)))
                    row.append((r, g, b))
                bg.append(row)

        ax.imshow(
            bg,
            extent=[x_min, x_max, y_min, y_max],
            origin="lower",
            alpha=0.42,
            zorder=0,
            aspect="auto",
        )

        # Optional light dust (less "starry sky" than pebble world).
        if show_sparkles and sparkle_count > 0:
            rng = random.Random((hash(tuple(labels)) ^ hash(title)) & 0xFFFFFFFF)
            sx = [rng.uniform(x_min, x_max) for _ in range(sparkle_count)]
            sy = [rng.uniform(-0.55, 0.75) for _ in range(sparkle_count)]
            ss = [rng.uniform(2, 10) for _ in range(sparkle_count)]
            ax.scatter(sx, sy, s=ss, c="white", alpha=0.05, linewidths=0, zorder=1)

        # Drop shadow.
        ax.scatter(
            [x + 0.05 for x in xs],
            [y - 0.06 for y in ys],
            s=[s * 1.05 for s in sizes],
            c="black",
            alpha=0.35,
            linewidths=0,
            zorder=2,
        )

        # Glow layers.
        for scale, alpha in ((1.90, 0.10), (1.55, 0.14), (1.25, 0.18)):
            ax.scatter(xs, ys, s=[s * scale for s in sizes], c=colors, alpha=alpha, linewidths=0, zorder=3)

        # Main pebbles.
        ax.scatter(
            xs,
            ys,
            s=sizes,
            c=colors,
            alpha=0.95,
            linewidths=1.6,
            edgecolors="white",
            zorder=4,
        )

        # Specular highlight.
        ax.scatter(
            [x - 0.06 for x in xs],
            [y + 0.06 for y in ys],
            s=[max(18, s * 0.14) for s in sizes],
            c="white",
            alpha=0.20,
            linewidths=0,
            zorder=5,
        )

        # Labels + optional probabilities.
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
                    facecolor="#111827",
                    edgecolor=outline_color,
                    linewidth=1.2,
                ),
                zorder=6,
            )

        if event is not None:
            p = self.probability(event)
            subtitle = f"P(event) = {p:.3f}   |   P(not event) = {1 - p:.3f}   |   |event| = {len(event_set)} of {n}"
        else:
            subtitle = "No event specified (showing full support)."

        ax.set_title(f"{title}\n{subtitle}", fontsize=16, fontweight="bold", pad=16, color=text_color)

        # Clean layout.
        ax.axhline(-0.05, color=outline_color, linewidth=1.2, alpha=0.9, zorder=1)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.axis("off")

        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    coin = NaiveSampleSpaceVisual(["H", "T"])
    print("Outcomes:", coin.support())
    print("P(H):", coin.probability(["H"]))
    print("P(T):", coin.probability(["T"]))
    print("P(H or T):", coin.probability(["H", "T"]))

    # Visualize the event {H} (close the plot window to let the script finish).
    coin.visualize(event=["H"], title="Coin flip: event = {H}")


