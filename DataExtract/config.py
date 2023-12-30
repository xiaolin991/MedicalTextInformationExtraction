# 配置文件
# 要分析的文本地址  文本编码格式:UTF-8  文本需要以“姓名”进行分割文本
text_filepath = 'data/text.txt'
excel_path = 'data/output.xlsx'
# 表头、要查找信息的正则、要存储信息的正则
#表项:用于Excel表头  正则：用于查找文本信息  正则：从查找的文本信息中保存需要的数据，填入Excel单元格
setting = [['姓名','姓名 [\u4e00-\u9fa5]{2,4}','[\u4e00-\u9fa5]{2,4}'],
           ['主动脉根部内径(mm)','主动脉 根部 内径 \\d{0,}mm','\\d+'],
           ['左房内径','左 房 内 径 \\d+mm','\\d+'],
           ['HR bpm','HR \\d+ bpm','\\d+'],
           ['FS %','FS \\d+ %','\\d+'],
           ['左室舒张末期内径 mm','左室舒张末期内径 \\d+mm','\\d+'],
           ['EF %','EF \\d+ %','\\d+'],
           ['左室收缩末期内径 mm','左室收缩末期内径 \\d+mm','\\d+'],
           ['室间隔厚度 mm','室 间 隔 厚度 \\d+mm','\\d+'],
           ['左室后壁厚度 mm','左 室 后 壁 厚度 \\d+mm','\\d+'],
           ['E峰 cm/s','E峰 = \\d+ cm/s','\\d+'],
           ['肺动脉收缩压 mmHg','肺动脉收缩压\\d+mmHg','\\d+'],
            ['左室后壁后方宽 mm','左室后壁后方宽\\d+mm','\\d+'],
           ['右室前壁前方宽 mm','右室前壁前方宽\\d+mm','\\d+'],
           ['上下径\\*左右径 mm','上下径\\*左右径：\\d+x\\d+mm','\\d+x\\d+']
          ]

