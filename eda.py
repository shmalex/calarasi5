from pandas.core.reshape import reshape

def make_dummy_columns(mdc_df, column_name, prefix='', append_columns=[]):
    dummies = reshape.get_dummies(mdc_df[column_name], prefix=prefix)
    arr_append(append_columns, dummies.columns)
    mdc_df = mdc_df.join(dummies)
    return mdc_df


def unique_to_numbers(udf, column_name):
    unique_list = udf[column_name].unique()
    if (column_name in map_dict):
        x = map_dict[column_name]
        max_id = np.max(list(x.values())) +1
        print(max_id)
        for uq in unique_list:
            if uq not in x:
                x[uq] = max_id
                max_id +=1
    else:
        map_dict[column_name] = { x:i for i, x in enumerate(unique_list) if len(str(x)) >0}
    uv = map_dict[column_name]
    udf[column_name] = udf[column_name].apply(p, convert_dtype=True, args=(uv,))
    return map_dict