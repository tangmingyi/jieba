import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

# USAGE = "usage:    python extract_tags.py [file name] -k [top k]"
#
# parser = OptionParser(USAGE)
# parser.add_option("-k", dest="topK")
# opt, args = parser.parse_args()
#
#
# if len(args) < 1:
#     print(USAGE)
#     sys.exit(1)

file_name = "jiebaTest.txt"

# if opt.topK is None:
#     topK = 10
# else:
#     topK = int(opt.topK)

content = open(file_name, 'rb').read()

tags_list = jieba.analyse.extract_tags(content, topK=10,withWeight=True,allowPOS=())#sentence:文本,
                                                    # topK=10：返回TF-VDF值最大的前10个,
                                                    #withWeight=False：是否返回权重值,
                                                    # allowPOS=()：只抽取某些词性的词
print(",".join(tags_list))