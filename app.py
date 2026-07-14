import streamlit as st
from utils.helpers import inject_custom_css
from components.sidebar import render_sidebar_header, render_sidebar_footer

# 1. Primary Page Configuration
# Note: Streamlit requires set_page_config to be the first Streamlit command.
st.set_page_config(
    page_title="SmartCampusAI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# 3. Dynamic Page Routing Declaration
# Unauthenticated Pages
login_page = st.Page("pages/login.py", title="Sign In", icon="🔐")
register_page = st.Page("pages/register.py", title="Register", icon="📝")

# Authenticated Pages
dashboard_page = st.Page("pages/dashboard.py", title="Admin Dashboard", icon="📊", default=True)
profile_page = st.Page("pages/profile.py", title="User Profile", icon="👤")
settings_page = st.Page("pages/settings.py", title="Settings", icon="⚙️")

# Route pages based on session validation
if st.session_state.logged_in:
    navigation_routes = [dashboard_page, profile_page, settings_page]
else:
    navigation_routes = [login_page, register_page]

# 4. Initialize Navigation
selected_route = st.navigation(navigation_routes, position="sidebar")

# 5. Apply Core Theme and UI Overrides
inject_custom_css()

# 6. Render Sidebar Brand
render_sidebar_header()

# 7. Render Sub-page Content
selected_route.run()

# 8. Render Sidebar Actions and Settings
render_sidebar_footer()
