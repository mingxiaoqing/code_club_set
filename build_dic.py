def nested_dict_builder(path_lst):
    """字典嵌套--构造目录树层级"""
    lst_base = [{}]
    for path in path_lst:
        lst_trend = lst_base
        dir_list = path.split('/')
        for dir_name in dir_list:
            if not dir_name:
                continue
            for trend_dic in lst_trend:
                if dir_name == trend_dic.get('name'):
                    lst_trend = trend_dic['children']
                else:
                    if not trend_dic:
                        trend_dic['name'] = dir_name
                        trend_dic['children'] = [{}]
                        lst_trend = trend_dic['children']
                    else:
                        lst_trend.append({'name': dir_name, 'children': [{}]})
                        lst_trend = lst_trend[-1]['children']
                break
    return lst_base



if __name__ == '__main__':
    lst = ['1/2/3/4', '1/2/22/33/4/55', '1/33/5/6/', '1/2/5/77/9', '1/4/6', '1/33/9/10']
    res = nested_dict_builder(lst)
    print(res[0])


# result
ss = {'name': '1',
      'children': [
          {'name': '2', 'children': [
              {'name': '3', 'children': [
                  {'name': '4', 'children': [{}]}]},
              {'name': '22', 'children': [
                  {'name': '33', 'children': [
                      {'name': '4', 'children': [
                          {'name': '55', 'children': [{}]}]}]}]},
              {'name': '5', 'children': [
                  {'name': '77', 'children': [
                      {'name': '9', 'children': [{}]}]}]}]},
          {'name': '33', 'children': [
              {'name': '5', 'children': [
                  {'name': '6', 'children': [{}]}]}]},
          {'name': '4', 'children': [
              {'name': '6', 'children': [{}]}]},
          {'name': '33', 'children': [
              {'name': '9', 'children': [
                  {'name': '10', 'children': [{}]}]}]}]}
