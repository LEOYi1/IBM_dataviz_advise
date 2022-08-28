# Import required libraries
!pip install dash
!pip install dash==1.19.0!
!pip install jupyter_dash
!pip install --upgrade plotly
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from jupyter_dash import JupyterDash
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update
