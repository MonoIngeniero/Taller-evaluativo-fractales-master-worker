from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT_DIR = Path(__file__).resolve().parent

EXP2_THREADS = [1, 2, 10, 64]
EXP2_T_SEC_MS = [77092, 84453, 77850, 76588]
EXP2_T_DIST_MS = [66241, 32636, 9224, 6848]

EXP3_WORKERS = [1, 2, 4]
EXP3_T_DIST_MS = [10146, 8017, 536]


def save_speedup_by_tile():
    labels = ["32x32 / N=2", "64x64 / N=4", "128x128 / N=8", "256x256 / N=16"]
    positions = range(len(labels))
    tile_speedup = [3.41, 3.41, 4.46, 4.53]
    fixed_count_speedup = [1.90, 3.45, 2.22, 1.47]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(positions, tile_speedup, marker="o", label="FixedTileSize")
    ax.plot(positions, fixed_count_speedup, marker="s", label="FixedCount")
    ax.set_title("Experimento 1: Speedup según estrategia de partición")
    ax.set_xlabel("Tamaño de baldosa (px) / número de tareas N")
    ax.set_ylabel("Speedup (x)")
    ax.set_xticks(list(positions), labels)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "speedup_vs_baldosa.png", dpi=160)
    plt.close(fig)


def save_speedup_by_threads():
    speedups = [
        sequential / distributed
        for sequential, distributed in zip(EXP2_T_SEC_MS, EXP2_T_DIST_MS)
    ]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(EXP2_THREADS, speedups, marker="o", label="Experimento 2")
    ax.set_title("Experimento 2: Speedup según hilos del worker")
    ax.set_xlabel("Hilos del worker (hilos)")
    ax.set_ylabel("Speedup (x)")
    ax.set_xticks(EXP2_THREADS)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "speedup_vs_hilos.png", dpi=160)
    plt.close(fig)


def save_speedup_by_workers():
    baseline = EXP3_T_DIST_MS[0]
    measured_speedups = [
        baseline / distributed for distributed in EXP3_T_DIST_MS
    ]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(
        EXP3_WORKERS,
        measured_speedups,
        marker="o",
        label="Speedup relativo medido",
    )
    ax.plot(EXP3_WORKERS, EXP3_WORKERS, linestyle="--", label="Ideal (S = p)")
    ax.set_title("Experimento 3: Speedup relativo según workers")
    ax.set_xlabel("Workers (p)")
    ax.set_ylabel("Speedup relativo (x)")
    ax.set_xticks(EXP3_WORKERS)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "speedup_vs_workers.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    save_speedup_by_tile()
    save_speedup_by_threads()
    save_speedup_by_workers()
