import plotly.express as px

def attribute_graph(sample_dict):
    # plots graph of number of attributes found per biosample 
    # sample_dict should have the format {sample_id: [attribute1, attribute2, ...]}
    attribute_count = {}

    for key, value in sample_dict.items():
        num_attrs = len(value)
    if num_attrs in attribute_count:
        attribute_count[num_attrs] += 1
    else:
        attribute_count[num_attrs] = 1


    bar_data = {"num_attributes": list(attribute_count.keys()), "num_samples": list(attribute_count.values()), "label": list(attribute_count.values())}
    fig = px.bar(bar_data, x="num_attributes", y="num_samples", text="label")
    fig.update_layout(title="Number of attributes found per biosample", xaxis=dict(title="# of attributes assigned to biosample"), yaxis=dict(title="Count"))
    fig.show()