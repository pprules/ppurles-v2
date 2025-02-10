import streamlit as st


def agenda():
    # Hero Section
    st.markdown('<h1 style="text-align: center;">Your Real Estate Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center;">Empowering Your Property Journey</h3>', unsafe_allow_html=True)

    # Main image and intro
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Ask me anything about our properties! 👋

        I can assist you with:
        - Finding homes within your budget 💰
        - Comparing different properties 🏠
        - Learning about neighborhoods 🌳
        - Getting property details instantly ⚡

        Just type your question in the chat below!
        """)
    with col2:
        st.image('./images/ai_real_estate.jpg')

    # Quick Start Guide
    st.markdown("### 💡 Try asking questions like:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Finding Properties")
        st.write("💬 'What homes are available under $500,000?'")
        st.write("💬 'Show me houses with 4 bedrooms'")
        st.write("💬 'Which properties have gardens?'")

    with col2:
        st.markdown("#### Comparing Options")
        st.write("💬 'What's the price range for 3-bedroom homes?'")
        st.write("💬 'Tell me about suburban properties'")
        st.write("💬 'Compare houses with large backyards'")

    # Features with simple icons
    st.markdown("### ✨ What Makes Our Assistant Special")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### 🎯 For Home Buyers
        - Quick answers about any property
        - Easy price comparisons
        - Neighborhood insights
        - Available 24/7
        """)

    with col2:
        st.markdown("""
        #### 🏆 For Real Estate Agents
        - Automatic property matching
        - Quick client responses
        - Easy listing management
        - More time for what matters
        """)

    # How it Works
    st.markdown("### 🤔 How It Works")
    st.markdown("""
    1. **Ask a Question** - Type anything about properties
    2. **Get Instant Answers** - AI finds the perfect matches
    3. **Explore Details** - Learn more about each property
    4. **Stay Informed** - Get updates on new listings
    """)

    # Success Metrics
    st.markdown("### 📈 Why People Love Our Assistant")
    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:
        st.metric("Fast Response", "2 seconds", "average response time")

    with metric_col2:
        st.metric("High Accuracy", "94%", "accuracy rate")

    with metric_col3:
        st.metric("Daily Interactions", "100+", "chats per day")

    # Get Started Section
    st.info("""
    ### 👋 Ready to Start?
    Click **"AI Chatbot Demo"** in the sidebar to start chatting!

    Need help? Just ask "How can you assist me?" in the chat.
    """)

    # Optional: Fun Facts
    with st.expander("🎈 Fun Facts About Our Assistant"):
        st.markdown("""
        - Can search through 1000+ properties in seconds
        - Speaks in plain English (no real estate jargon!)
        - Updates property info in real-time
        - Remembers your preferences for better recommendations
        """)