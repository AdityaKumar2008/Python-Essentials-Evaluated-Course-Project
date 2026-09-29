# mainNPC.py
import streamlit as st
import matplotlib.pyplot as plt
from generatorNPC import build_character
from visualizerNPC import draw_radar, draw_gauge
from schemasNPC import col_palette, icon_map

# setup page layout
st.set_page_config(page_title="NPC Generator", page_icon="🎭", layout="wide")

def render_sidebar():
    sb = st.sidebar
    sb.title("🧙‍♂️ NPC Generator")
    sb.caption("Create unique characters with personalities, stories and statistics.")
    
    sb.subheader("⚙️ Generator Settings")
    w = sb.selectbox("Choose World", ["Fantasy", "Modern", "Cyberpunk", "Sci-Fi", "Steampunk"], index=0)
    ch = sb.slider("Chaos Level", min_value=1, max_value=10, value=5, help="Higher chaos = stranger characters.")
    btn = sb.button("✨ GENERATE NPC", use_container_width=True)
    
    sb.divider()
    sb.subheader("ℹ️ About")
    sb.write("NPC Generator creates characters using connected occupation, personality and stat generation rules.")
    sb.write("🌍 **World:** " + str(w))
    sb.write("🔥 **Chaos Level:** " + str(ch) + "/10")
    
    return w, ch, btn

def main():
    world_setting, chaos_val, gen_btn = render_sidebar()
    
    if ("curr_npc" not in st.session_state) or gen_btn:
        st.session_state["curr_npc"] = build_character()
        
    npc = st.session_state["curr_npc"]
    
    c1, c2 = st.columns([1.6, 1], gap="large")
    
    with c1:
        st.header("{} ✦".format(npc["full_name"]))
        st.caption("Age {} • {}".format(npc["age"], npc["job"]))
        
        tc1, tc2, tc3 = st.columns(3)
        tc1.info("🏰 World: {}".format(world_setting))
        tc2.info("🔥 Chaos: {}/10".format(chaos_val))
        tc3.info("🎭 Personality: {}".format(npc["personality"]))
        
        st.write("_{}_".format(npc["quote"]))
        st.divider()
        
        ic1, ic2, ic3 = st.columns(3)
        ic1.subheader("❤️ Likes")
        ic1.write(npc["likes"])
        
        ic2.subheader("💔 Dislikes")
        ic2.write(npc["dislikes"])
        
        ic3.subheader("🎯 Goal")
        ic3.write(npc["goal"])
        
        st.subheader("🎨 Hobby")
        st.write("**{}** enjoys **{}**.".format(npc["full_name"], npc["hobby"]))
        
        with st.container(border=True):
            st.subheader("🔒 Classified Information")
            st.write(npc["secret"])
            
    with c2:
        with st.container(border=True):
            st.subheader("👤 Personality Profile")
            r_fig = draw_radar(npc["stats"])
            st.pyplot(r_fig, use_container_width=True)
            plt.close(r_fig)
            
    st.divider()
    
    st.subheader("📊 Character Stats")
    
    g_cols = st.columns(5)
    stat_keys = list(npc["stats"].keys())
    
    for idx in range(len(stat_keys)):
        k = stat_keys[idx]
        v = npc["stats"][k]
        
        with g_cols[idx]:
            with st.container(border=True):
                st.caption("%s %s" % (icon_map[k], k))
                g_fig = draw_gauge(v, col_palette[k])
                st.pyplot(g_fig, use_container_width=True)
                plt.close(g_fig)
                
    st.divider()
    
    st.subheader("⭐ Character Overview")
    
    stat_sum = 0
    for key in stat_keys:
        stat_sum = stat_sum + npc["stats"][key]
        
    avg = int(round(stat_sum / float(len(stat_keys))))
    
    if avg >= 80:
        desc = "Exceptional"
    elif avg >= 65:
        desc = "Highly Capable"
    elif avg >= 50:
        desc = "Balanced"
    else:
        desc = "Unpredictable"
        
    oc1, oc2 = st.columns(2)
    oc1.write("**Overall Profile:** " + desc)
    oc2.write("**Overall stat average:** %d/100" % avg)
    
    st.progress(avg / 100.0)

if __name__ == "__main__":
    main()