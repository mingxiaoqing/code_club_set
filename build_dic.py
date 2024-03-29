def nested_dict_builder(dir_list, lst_trend):
    """字典嵌套--构造目录树层级"""
    num = len(dir_list)
    for dir_name in dir_list:
        num -= 1
        if not dir_name:
            continue
        trend_dic = lst_trend[0]
        if not trend_dic:
            trend_dic['name'] = dir_name
            if num:
                trend_dic['children'] = [{}]
                lst_trend = trend_dic['children']
            continue
        if dir_name == trend_dic.get('name'):
            lst_trend = trend_dic['children']
            continue

        index = [i for i, item in enumerate(lst_trend) if item['name'] == dir_name]
        if index:
            lst_trend = lst_trend[index[0]]['children']
        else:
            if num:
                lst_trend.append({'name': dir_name, 'children': [{}]})
                lst_trend = lst_trend[-1]['children']
            else:
                lst_trend.append({'name': dir_name})


if __name__ == '__main__':
    path_lst = ['1/2/3/4', '1/2/22/33/4/55', '1/33/5/6/', '1/2/5/77/9', '1/4/6', '1/33/9/10']
    lst_base = [{}]
    for path in path_lst:
        dir_list = path.strip('/ ').split('/')
        nested_dict_builder(dir_list, lst_base)
    print(lst_base)

dd = {
    'name': '1', 'children': [
        {'name': '2', 'children': [
            {'name': '3', 'children': [
                {'name': '4'}]},
            {'name': '22', 'children': [
                {'name': '33', 'children': [
                    {'name': '4', 'children': [
                        {'name': '55'}]}]}]},
            {'name': '5', 'children': [
                {'name': '77', 'children': [
                    {'name': '9'}]}]}]},
        {'name': '33', 'children': [
            {'name': '5', 'children': [
                {'name': '6'}]},
            {'name': '9', 'children': [
                {'name': '10'}]}]},
        {'name': '4', 'children': [
            {'name': '6'}]}]}
