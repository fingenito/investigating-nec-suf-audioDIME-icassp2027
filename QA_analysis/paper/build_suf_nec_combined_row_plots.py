"""
Come build_suf_nec_combined_plots.py, ma con i tre pannelli (complete,
audio_only, text_only) affiancati in un'unica figura per modello, con
UNA sola legenda condivisa in alto (invece di ripeterla tre volte).
Produce un solo file per modello: qwen_suf_nec_combined_row.pdf/.png e
af3_suf_nec_combined_row.pdf/.png.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from build_suf_nec_plots import CONDITIONS, load_long, K_MAX
from build_suf_nec_combined_plots import (
    COLOR_SUFFICIENCY, COLOR_NECESSITY,
    FEATURE_ORDER, FEATURE_LABELS, FEATURE_MARKERS, FEATURE_OFFSETS,
    CAPSIZE, ERR_LW, MARKER_SIZE, LINE_LW,
    mean_se_by_k,
)

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures_suf_nec")
os.makedirs(OUT_DIR, exist_ok=True)

PANEL_TITLES = {"complete": "(a) Complete", "audio_only": "(b) Audio only", "text_only": "(c) Text only"}
PANEL_ORDER = ["complete", "audio_only", "text_only"]


def style_axis(ax, show_ylabel: bool, y_max: float = 1.1):
    ax.axhline(0.5, color="#999999", linestyle="--", linewidth=0.9, zorder=1)
    ax.set_xlim(0.5, K_MAX + 0.5)
    ax.set_xticks(range(2, K_MAX + 1, 2))
    ax.set_ylim(0.0, y_max)
    yticks = [t / 10 for t in range(0, int(round(y_max * 10)) + 1, 2)]
    ax.set_yticks(yticks)
    if not show_ylabel:
        ax.tick_params(labelleft=False)
    sns.despine(ax=ax)


def draw_panel(ax, df):
    sub = df[df["correct_baseline"] == True].dropna(subset=["sufficiency_score", "necessity_score"])
    sub = sub[sub["feature_source"].isin(FEATURE_ORDER)]

    for feat in FEATURE_ORDER:
        fsub = sub[sub["feature_source"] == feat]
        off = FEATURE_OFFSETS[feat]
        marker = FEATURE_MARKERS[feat]

        k_s, mean_s, sem_s = mean_se_by_k(fsub, "sufficiency_score")
        ax.errorbar(
            k_s + off, mean_s, yerr=sem_s,
            fmt=marker, color=COLOR_SUFFICIENCY, ecolor=COLOR_SUFFICIENCY,
            linestyle="-", linewidth=LINE_LW, markersize=MARKER_SIZE,
            capsize=CAPSIZE, capthick=ERR_LW, elinewidth=ERR_LW,
            markeredgecolor="white", markeredgewidth=0.4, zorder=3,
        )

        k_n, mean_n, sem_n = mean_se_by_k(fsub, "necessity_score")
        ax.errorbar(
            k_n + off, mean_n, yerr=sem_n,
            fmt=marker, color=COLOR_NECESSITY, ecolor=COLOR_NECESSITY,
            linestyle="-", linewidth=LINE_LW, markersize=MARKER_SIZE,
            capsize=CAPSIZE, capthick=ERR_LW, elinewidth=ERR_LW,
            markeredgecolor="white", markeredgewidth=0.4, zorder=3,
        )


def plot_model_row(model: str, out_path: str, y_max: float = 1.1):
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.1), sharey=True)

    for i, condition in enumerate(PANEL_ORDER):
        ax = axes[i]
        df = load_long(CONDITIONS[(model, condition)])
        draw_panel(ax, df)
        ax.set_xlabel("k (top-ranked features)")
        if i == 0:
            ax.set_ylabel("Score")
        style_axis(ax, show_ylabel=(i == 0), y_max=y_max)
        ax.set_title(PANEL_TITLES[condition], fontsize=11, pad=6)

    # Legenda 1: colore -> metrica
    metric_handles = [
        plt.Line2D([0], [0], color=COLOR_SUFFICIENCY, lw=1.8, marker="o", markersize=5,
                   markerfacecolor=COLOR_SUFFICIENCY, markeredgecolor="white", label="Sufficiency"),
        plt.Line2D([0], [0], color=COLOR_NECESSITY, lw=1.8, marker="o", markersize=5,
                   markerfacecolor=COLOR_NECESSITY, markeredgecolor="white", label="Necessity"),
    ]
    legend1 = fig.legend(
        handles=metric_handles, loc="upper center", bbox_to_anchor=(0.34, 1.04),
        ncol=2, frameon=False, handlelength=2.0,
    )
    fig.add_artist(legend1)

    # Legenda 2: marker -> feature source
    feature_handles = [
        plt.Line2D([0], [0], color="#444444", linestyle="none", marker=FEATURE_MARKERS[f], markersize=6,
                   markerfacecolor="#444444", markeredgecolor="#444444", label=FEATURE_LABELS[f])
        for f in FEATURE_ORDER
    ]
    fig.legend(
        handles=feature_handles, loc="upper center", bbox_to_anchor=(0.72, 1.04),
        ncol=3, frameon=False, handlelength=1.5, handletextpad=0.8,
    )

    fig.tight_layout()
    fig.savefig(out_path, bbox_inches="tight")
    fig.savefig(out_path.replace(".pdf", ".png"), bbox_inches="tight")
    plt.close(fig)


def main():
    Y_MAX_BY_MODEL = {"qwen": 1.4, "af3": 1.1}
    for model in ["qwen", "af3"]:
        out = os.path.join(OUT_DIR, f"{model}_suf_nec_combined_row.pdf")
        print(f"Genero {model} (complete/audio_only/text_only)...")
        plot_model_row(model, out, y_max=Y_MAX_BY_MODEL[model])
        print(f"  salvato: {out}")

    print(f"\nFatto. Figure in: {OUT_DIR}")


if __name__ == "__main__":
    main()
