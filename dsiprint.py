import numpy as np
from IPython.display import HTML, display

def df_info(df):
    tprint(['{0} rows  by {1} cols'.format(*df.shape)])
    hprint('data frame head', color='black', h=4)
    print(df.head())
    hprint('data describe ', color='black', h=4)
    print(df.describe())
    hprint('data Info ', color='black', h=4)
    print(df.info())

def hmap(data):
    d = data
    if len(np.shape(data)) == 1:
        d = [d]

    def a_color(string):
        return 'background: rgba(255, 0, 0, {0:3})!important;'.format(string)

    def color(string):
        red = int(round(string * 255))
        hex_red = '{:02x}'.format(red)
        green = 255  # int(round(255-(string*255)))
        hex_green = '{:02x}'.format(green)
        c = '#' + hex_red + '00' + hex_green
        return "background-color:" + c + ";"

    display(HTML(
        '<table><tr style="background: #fff;">{}</tr></table>'.format('</tr><tr  style="background: #fff;">'.join(
            '<td style="{1}">{0:10}</td>'.format('</td><td>'.join(str(_) for _ in row), a_color(row[1])) for row in d)
        )
    ))


def tprint(data):
    d = data
    if len(np.shape(data)) == 1:
        d = [d]
    display(HTML(
        '<table><tr>{}</tr></table>'.format(
            '</tr><tr>'.join(
                '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in d)
        )
    ))


def hprint(msg, color='red', h=3, style='normal'):
    display(HTML('<h{2} style="color:{1}; font-style:{3};">{0}</h{2}>'.format(msg, color, h, style)))

def iprint(msg):
    hprint(msg, style='italic', color='gray', h=4)

def arr_remove(arr, vals):
    return [x for x in arr if x not in vals]


def arr_append(arr, vals):
    for val in vals:
        arr.append(val)
    return arr


def make_dummy_columns(mdc_df, column_name, prefix='', append_columns=[]):
    dummies = reshape.get_dummies(mdc_df[column_name], prefix=prefix)
    arr_append(append_columns, dummies.columns)
    mdc_df = mdc_df.join(dummies)
    # tprint(append_columns)
    return mdc_df


def parse_year(string):
    idx = 0
    if (string[5] == '/'):
        idx = 6
    elif (string[4] == '/'):
        idx = 5
    elif (string[3] == '/'):
        idx = 4
    b = np.int16(string[idx:(idx + 4)])
    # print(b)
    return b


def p(val, dic):
    if val in dic:
        return dic[val] * 1
    return -1  # len(dic) * (-1)


def unique_to_numbers(udf, column_name):
    unique_list = udf[column_name].unique()
    if (column_name in map_dict):
        x = map_dict[column_name]
        max_id = np.max(list(x.values())) + 1
        print(max_id)
        for uq in unique_list:
            if uq not in x:
                x[uq] = max_id
                max_id += 1
    else:
        map_dict[column_name] = {x: i for i, x in enumerate(
            unique_list) if len(str(x)) > 0}
    uv = map_dict[column_name]
    udf[column_name] = udf[column_name].apply(
        p, convert_dtype=True, args=(uv,))
    return map_dict


def print_apr(y_test, y_predict):
    tprint(
        [['Accuracy Score: ', accuracy_score(y_test, y_predict)],
         ['Precision tp / (tp + fp): ', precision_score(y_test, y_predict)],
         ['Recall tp / (tp + fn): ', recall_score(y_test, y_predict)]])
