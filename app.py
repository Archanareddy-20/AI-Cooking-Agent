import streamlit as st
from agents.head_chef import head_chef_agent
from agents.prep_cook import prep_cook_agent
from agents.food_critic import food_critic_agent

st.set_page_config(page_title="AI Cooking Agent with HITL", layout="wide")
st.title("👨‍🍳 AI Cooking Agent with HITL Flow")
st.write("Approve or edit each step before the next agent runs")

# --- 1. FLOWCHART FUNCTION ---
def draw_flowchart(step):
    steps = ["Start", "Head Chef", "HITL #1", "Prep Cook", "HITL #2", "Food Critic", "Done"]
    nodes = ""
    edges = ""
    
    for i, s in enumerate(steps):
        # Current step = Green, Done = Blue, Future = Gray
        if i < step:
            color = "fill:#ADD8E6,stroke:#333,stroke-width:2px" # Done
        elif i == step:
            color = "fill:#90EE90,stroke:#333,stroke-width:3px" # Current
        else:
            color = "fill:#F0F0F0,stroke:#999" # Future
        
        nodes += f' {i}["{s}"]:::{color}\n'
        if i > 0:
            edges += f' {i-1} --> {i}\n'
    
    graph = f"graph LR\n{nodes}{edges}"
    st.graphviz_chart(graph)

# --- 2. SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'recipe' not in st.session_state:
    st.session_state.recipe = ""
if 'prep' not in st.session_state:
    st.session_state.prep = ""
if 'dish' not in st.session_state:
    st.session_state.dish = ""

# --- 3. INPUT ---
dish_input = st.text_input("What dish do you want to cook?")
if dish_input:
    st.session_state.dish = dish_input

draw_flowchart(st.session_state.step) # Draw flowchart
st.divider()

col1, col2 = st.columns([1,3])

with col1:
    if st.button("🔄 Reset All", use_container_width=True):
        st.session_state.step = 0
        st.session_state.recipe = ""
        st.session_state.prep = ""
        st.rerun()

# --- 4. AGENT FLOW WITH HITL ---

# STEP 0: START
if st.session_state.step == 0 and st.session_state.dish:
    if st.button("▶️ Start Cooking Team", type="primary", use_container_width=True):
        st.session_state.step = 1
        st.rerun()

# STEP 1: HEAD CHEF
if st.session_state.step == 1:
    with st.spinner("Head Chef is cooking up a recipe..."):
        st.session_state.recipe = head_chef_agent(st.session_state.dish)
    st.write(st.session_state.recipe)
    
    if st.button("✅ Approve & Send to Prep Cook", type="primary"):
        st.session_state.step = 2 # Go to HITL
        st.rerun()

# STEP 2: HITL 1 - APPROVE/EDIT RECIPE
if st.session_state.step == 2:
    st.info("👆 **HITL #1**: Review Head Chef's recipe. Edit it if needed, then approve.")
    edited_recipe = st.text_area("Edit Recipe:", st.session_state.recipe, height=300)
    
    if st.button("✅ Approve Recipe & Continue", type="primary"):
        st.session_state.recipe = edited_recipe
        st.session_state.step = 3
        st.rerun()

# STEP 3: PREP COOK
if st.session_state.step == 3:
    with st.spinner("Prep Cook is making shopping list..."):
        st.session_state.prep = prep_cook_agent(st.session_state.dish)
    st.write(st.session_state.prep)
    
    if st.button("✅ Approve & Send to Food Critic", type="primary"):
        st.session_state.step = 4 # Go to HITL
        st.rerun()

# STEP 4: HITL 2 - FINAL CHECK
if st.session_state.step == 4:
    st.info("👆 **HITL #2**: Final check before Food Critic reviews it.")
    st.write("**Final Recipe being sent:**")
    st.code(st.session_state.recipe)
    
    if st.button("✅ Send to Food Critic", type="primary"):
        st.session_state.step = 5
        st.rerun()

# STEP 5: FOOD CRITIC
if st.session_state.step == 5:
    with st.spinner("Food Critic is tasting..."):
        review = food_critic_agent(st.session_state.dish, st.session_state.recipe)
    st.write(review)
    
    st.session_state.step = 6 # Done

# STEP 6: DONE
if st.session_state.step == 6:
    st.success("🎉 Cooking Process Complete!")
    st.balloons()