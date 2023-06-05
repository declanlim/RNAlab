import plotly.express as px

def attribute_graph(sample_dict):
    # plots graph of number of attributes found per biosample 
    # sample_dict should have the format {sample_id: [attribute1, attribute2, ...]}
    attribute_count = {}

    for value in sample_dict.values():
        if value is None:
            num_attrs = 0
        else:
            num_attrs = len(value)
        if num_attrs in attribute_count:
            attribute_count[num_attrs] += 1
        else:
            attribute_count[num_attrs] = 1


    bar_data = {'num_attributes': list(attribute_count.keys()), 'num_samples': list(attribute_count.values()), 'label': list(attribute_count.values())}
    fig = px.bar(bar_data, x='num_attributes', y='num_samples', text='label')
    fig.update_layout(title='Number of attributes found per biosample', xaxis=dict(title='# of attributes assigned to biosample'), yaxis=dict(title='Count'))
    fig.show()

def matches_graph(sample_dict):
    # plots a graph of number of samples matched to BRENDA vs number of samples not matched to BRENDA
    no_match_count = list(sample_dict.values()).count(None)
    match_count = 10000 - no_match_count

    bar_data = {'match': ['Match', 'No match'], 'count': [match_count, no_match_count], 'label': [match_count, no_match_count]}
    fig = px.bar(bar_data, x='match', y='count', text='label')
    fig.update_layout(title='Number of Samples Matched to Brenda', xaxis=dict(title='Match'), yaxis=dict(title='Count'))
    fig.show()


def attribute_name_graph(attribute_dict):
    # plot a graph of the counts of each attribute name that the BRENDA term was mapped to
    # attribute_dict has the format {biosample_id, attirbute_name}

    attribute_count = {}
    for value in attribute_dict.values():
        if value in attribute_count:
            attribute_count[value] += 1
        else:
            attribute_count[value] = 1
    bar_data = {'attribute': list(attribute_count.keys()), 'count': list(attribute_count.values()), 'label': list(attribute_count.values())}
    fig = px.bar(bar_data, x='attribute', y='count', text='label')
    fig.update_layout(title='Counts for found attributes', xaxis=dict(title='Attribute'), yaxis=dict(title='Count'))
    fig.show()