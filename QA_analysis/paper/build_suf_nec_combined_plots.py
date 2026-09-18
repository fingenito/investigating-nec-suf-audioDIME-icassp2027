"""
Un solo pannello per condizione/modello che mostra INSIEME sufficienza e
necessita' di UC_text, UC_audio, MI (solo campioni corretti), usando:
  - colore  -> metrica (sufficiency / necessity)
  - marker  -> feature source (UC_text / UC_audio / MI)
Stile, scala, font identici a build_suf_nec_plots.py; qui cambia solo la
codifica visiva (colore+marker invece di solo colore) per stare in un unico
pannello anziche' due.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from build_suf_nec_plots import CONDITIONS, load_long, K_MAX

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures_suf_nec")
os.makedirs(OUT_DIR, exist_ok=True)

# Colore = metrica (deliberatamente diverso dalla palette feature-source usata
# altrove, per non far pensare che "blu"/"rosso" qui significhino testo/MI).
COLOR_SUFFICIENCY = "#2C6E8C"  # blu acciaio spento
COLOR_NECESSITY = "#B23A2E"    # rosso mattone spento

# Marker = feature source.
FEATURE_ORDER = ["UC_text", "UC_audio", "MI"]
FEATURE_LABELS = {"UC_text": "UC$_{text}$", "UC_audio": "UC$_{audio}$", "MI": "MI"}
FEATURE_MARKERS = {"UC_text": "o", "UC_audio": "s", "MI": "^"}
FEATURE_OFFSETS = {"UC_text": -0.15, "UC_audio": 0.0, "MI": 0.15}

CAPSIZE = 3
ERR_LW = 1.0
MARKER_SIZE = 5.0
LINE_LW = 1.3


def style_axis(ax):
    ax.axhline(0.5, color="#999999", linestyle="--", linewidth=0.9, zorder=1)
    ax.set_xlim(0.5, K_MAX + 0.5)
    ax.set_xticks(range(2, K_MAX + 1, 2))
    ax.set_ylim(0.0, 1.1)
    ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    import seaborn as sns
    sns.despine(ax=ax)


def mean_se_by_k(sub, ycol):
    stats = sub.groupby("k")[ycol].agg(["mean", "sem"]).reset_index().sort_values("k")
    return stats["k"].to_numpy(), stats["mean"].to_numpy(), stats["sem"].to_numpy()


def plot_combined(df, out_path):
    sub = df[df["correct_baseline"] == True].dropna(subset=["sufficiency_score", "necessity_score"])
    sub = sub[sub["feature_source"].isin(FEATURE_ORDER)]

    fig, ax = plt.subplots(1, 1, figsize=(4.6, 3.3))

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

    ax.set_xlabel("k (top-ranked features)")
    ax.set_ylabel("Score")
    style_axis(ax)

    # Legenda 1: colore -> metrica
    metric_handles = [
        plt.Line2D([0], [0], color=COLOR_SUFFICIENCY, lw=1.8, marker="o", markersize=5,
                   markerfacecolor=COLOR_SUFFICIENCY, markeredgecolor="white", label="Sufficiency"),
        plt.Line2D([0], [0], color=COLOR_NECESSITY, lw=1.8, marker="o", markersize=5,
                   markerfacecolor=COLOR_NECESSITY, markeredgecolor="white", label="Necessity"),
    ]
    legend1 = fig.legend(
        handles=metric_handles, loc="upper center", bbox_to_anchor=(0.30, 1.14),
        ncol=1, frameon=False, handlelength=2.0, title="Metric", alignment="left",
    )
    fig.add_artist(legend1)

    # Legenda 2: marker -> feature source (neutro, grigio scuro)
    feature_handles = [
        plt.Line2D([0], [0], color="#444444", linestyle="none", marker=FEATURE_MARKERS[f], markersize=6,
                   markerfacecolor="#444444", markeredgecolor="#444444", label=FEATURE_LABELS[f])
        for f in FEATURE_ORDER
    ]
    fig.legend(
        handles=feature_handles, loc="upper center", bbox_to_anchor=(0.72, 1.14),
        ncol=1, frameon=False, handlelength=1.5, handletextpad=1.2, title="Feature", alignment="left",
    )

    fig.tight_layout()
    fig.savefig(out_path, bbox_inches="tight")
    fig.savefig(out_path.replace(".pdf", ".png"), bbox_inches="tight")
    plt.close(fig)


def main():
    for (model, condition), path in CONDITIONS.items():
        print(f"Carico {model} / {condition} ...")
        df = load_long(path)
        out = os.path.join(OUT_DIR, f"{model}_{condition}_suf_nec_combined.pdf")
        plot_combined(df, out)
        print(f"  salvato: {out}")

    print(f"\nFatto. Figure combinate in: {OUT_DIR}")


if __name__ == "__main__":
    main()
