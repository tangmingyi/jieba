# import sys
# sys.path.append('../')
#
# import jieba
import jieba.analyse
# from optparse import OptionParser

# USAGE = "usage:    python extract_tags_idfpath.py [file name] -k [top k]"
#
# parser = OptionParser(USAGE)
# parser.add_option("-k", dest="topK")
# opt, args = parser.parse_args()
#
#
# if len(args) < 1:
#     print(USAGE)
#     sys.exit(1)
#
# file_name = args[0]
#
# if opt.topK is None:
#     topK = 10
# else:
#     topK = int(opt.topK)

content = open("jiebaTest.txt", 'rb').read()

# jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")#设置停止词文件位置
jieba.analyse.set_idf_path("my_corpos.txt")                    #设置语料库位置 坑一：语料库只有两个参数：词和词频

tagsList = jieba.analyse.extract_tags(content, topK=10,withWeight=False,allowPOS=())#坑二：withweight设置为True时小心下面的print格式

print(",".join(tagsList))     