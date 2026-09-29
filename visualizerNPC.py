# visualizerNPC.py
import matplotlib.pyplot as plt
import numpy as np

def draw_radar(s_dict):
    keys = list(s_dict.keys())
    vals = list(s_dict.values())
    vals.append(vals[0])
    
    rads = np.linspace(0, 2 * np.pi, len(keys) + 1)
    
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw={"polar": True})
    ax.plot(rads, vals, color="#6366f1", linewidth=2)
    ax.fill(rads, vals, color="#818cf8", alpha=0.3)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(rads[:-1])
    ax.set_xticklabels(keys)
    plt.ylim(0, 100)
    plt.tight_layout()
    return fig

def draw_gauge(val, color_code):
    fig, ax = plt.subplots(figsize=(2, 2))
    p_data = [val, 100 - val]
    c_data = [color_code, "#e2e8f0"]
    
    ax.pie(p_data, colors=c_data, startangle=90, counterclock=False, wedgeprops=dict(width=0.3, edgecolor="none"))
    ax.text(0, 0, "%d%%" % val, ha="center", va="center", fontsize=12, fontweight="bold")
    plt.tight_layout()
    return fig