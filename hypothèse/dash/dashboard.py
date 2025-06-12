from dash import Dash, html, dash_table, dcc, Input, Output
import pandas as pd
import os

# Load the data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "enquete_sur_le_bonheur.csv")
df_bonheur = pd.read_csv(csv_path, sep=';')
df_bonheur.rename(columns={
    df_bonheur.columns[0]: 'date',
    df_bonheur.columns[1]: 'sex',
    df_bonheur.columns[2]: 'age',
    df_bonheur.columns[3]: 'dpt',
    df_bonheur.columns[4]: 'happyness',
    df_bonheur.columns[5]: 'temp',
    df_bonheur.columns[6]: 'work',
    df_bonheur.columns[7]: 'money',
    df_bonheur.columns[8]: 'nature',
    df_bonheur.columns[9]: 'personal_time',
    df_bonheur.columns[10]: 'sports',
    df_bonheur.columns[11]: 'art',
    df_bonheur.columns[12]: 'health',
    df_bonheur.columns[13]: 'personal'
}, inplace=True)

# Initialize the app
app = Dash()

# App layout
app.layout = html.Div([
    html.H1("Enquête sur le Bonheur"),
    html.Div([
        html.Label("Sélectionnez une colonne:"),
        dash_table.DataTable(
            id='table-bonheur',
            columns=[{"name": i, "id": i} for i in df_bonheur.columns],
            data=df_bonheur.to_dict('records'),
            page_size=10,
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
            style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
        )
    ]),
    html.Div([
        html.Label("Select a value:"),
        dcc.Dropdown(
            id='some-input',
            options=[{'label': i, 'value': i} for i in df_bonheur['happyness'].unique()],
            value=df_bonheur['happyness'].unique()[0]
        )
    ])
])

# Single callback to update the table
@app.callback(
    Output('table-bonheur', 'data'),
    Input('some-input', 'value')
)
def update_table(selected_value):
    filtered_df = df_bonheur[df_bonheur['happyness'] == selected_value]
    return filtered_df.to_dict('records')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)



