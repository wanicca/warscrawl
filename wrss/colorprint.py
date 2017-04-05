#coding=utf8
class Colored(object):
    control =''
    disp=''
    fore=''
    back=''

    def __init__ (self, *args):
        if(len(args)==0):
            self.control='\033[0m'
        elif(len(args)==1):
            self.control=args[0]
        else:
            self.disp=args[0]
            self.fore=args[1]
            if(len(args)==3):self.back=args[2]
            self.control='\033[%s%s%sm'%(self.disp,self.fore,self.back)

    def __call__(self,s):
        self.cprint(s)

    def cprint(self,s):
        print('%s%s%s'%(self.control,s,'\033[0m'))

DEFAULTCOLORED=Colored()

def DEFAULT(option=DEFAULTCOLORED):
    return Colored('0;',option.fore,option.back)

def BOLD(option=DEFAULTCOLORED):
    return Colored('1;',option.fore,option.back)

def UNDERLINE(option=DEFAULTCOLORED):
    return Colored('4;',option.fore,option.back)

def BLINK(option=DEFAULTCOLORED):
    return Colored('5;',option.fore,option.back)

def INVERSE(option=DEFAULTCOLORED):
    return Colored('7;',option.fore,option.back)

def INVISIBLE(option=DEFAULTCOLORED):
    return Colored('8;',option.fore,option.back)

def NOTBOLD(option=DEFAULTCOLORED):
    return Colored('22;',option.fore,option.back)

def NOTUNDERLINE(option=DEFAULTCOLORED):
    return Colored('24;',option.fore,option.back)

def NOTBLINK(option=DEFAULTCOLORED):
    return Colored('25;',option.fore,option.back)

def BLACK(option=DEFAULTCOLORED):
    return Colored(option.disp,'30',option.back)

def RED(option=DEFAULTCOLORED):
    return Colored(option.disp,'31',option.back)

def GREEN(option=DEFAULTCOLORED):
    return Colored(option.disp,'32',option.back)

def YELLOW(option=DEFAULTCOLORED):
    return Colored(option.disp,'33',option.back)

def BLUE(option=DEFAULTCOLORED):
    return Colored(option.disp,'34',option.back)

def PURPLE(option=DEFAULTCOLORED):
    return Colored(option.disp,'35',option.back)

def CYAN(option=DEFAULTCOLORED):
    return Colored(option.disp,'36',option.back)

def WHITE(option=DEFAULTCOLORED):
    return Colored(option.disp,'37',option.back)

def BLACKBACK(option=DEFAULTCOLORED):
    return Colored(option.disp,option.fore,';40')

def REDBACK(option=DEFAULTCOLORED):
    return Colored(option.disp,option.fore,';41')

def GREENBACK(option=DEFAULTCOLORED):
    return Colored(option.disp,option.fore,';42')

def YELLOWBACK(option=DEFAULTCOLORED):
    return Colored(option.disp,option.fore,';43')

def BLUEBACK(option=DEFAULTCOLORED):
    return Colored(option.disp,option.fore,';44')

def PURPLEBACK(option=DEFAULTCOLORED):
    return Colored(option.disp,option.fore,';45')

def CYANBACK(option=DEFAULTCOLORED):
    return Colored(option.disp,option.fore,';46')

def WHITEBACK(option=DEFAULTCOLORED):
    return Colored(option.disp,option.fore,';47')

# ------------------------------------------------
#   python终端显示彩色字符类，可以调用不同的方法
# 选择不同的颜色.使用方法看示例代码就很容易明白.
# ------------------------------------------------
#
# 显示格式: \033[显示方式;前景色;背景色m
# ------------------------------------------------
# 显示方式             说明
#   0                 终端默认设置
#   1                 高亮显示
#   4                 使用下划线
#   5                 闪烁
#   7                 反白显示
#   8                 不可见
#   22                非粗体
#   24                非下划线
#   25                非闪烁
#
#   前景色             背景色            颜色
#     30                40              黑色
#     31                41              红色
#     32                42              绿色
#     33                43              黃色
#     34                44              蓝色
#     35                45              紫红色
#     36                46              青蓝色
#     37                47              白色
# ------------------------------------------------

    # # 显示格式: \033[显示方式;前景色;背景色m
    # # 只写一个字段表示前景色,背景色默认
    # RED = '\033[31m'       # 红色
    # GREEN = '\033[32m'     # 绿色
    # YELLOW = '\033[33m'    # 黄色
    # BLUE = '\033[34m'      # 蓝色
    # FUCHSIA = '\033[35m'   # 紫红色
    # CYAN = '\033[36m'      # 青蓝色
    # WHITE = '\033[37m'     # 白色
    # #: no color
    # RESET = '\033[0m'      # 终端默认颜色

    # def color_str(self, color, s):
    #     return '{}{}{}'.format(
    #         getattr(self, color),
    #         s,
    #         self.RESET
    #     )
    #
    # def red(self, s):
    #     return self.color_str('RED', s)
    #
    # def green(self, s):
    #     return self.color_str('GREEN', s)
    #
    # def yellow(self, s):
    #     return self.color_str('YELLOW', s)
    #
    # def blue(self, s):
    #     return self.color_str('BLUE', s)
    #
    # def fuchsia(self, s):
    #     return self.color_str('FUCHSIA', s)
    #
    # def cyan(self, s):
    #     return self.color_str('CYAN', s)
    #
    # def white(self, s):
    #     return self.color_str('WHITE', s)
    #


# def cprint(s,*args):
#     if(len(args)>=1):
#         pre = '\033['
#         if(len(args)==1):
#             pre = '%s3%d'%(pre,args[0])
#         elif(len(args)==2):
#             pre = '%s%d;3%d'%(pre,args[0],args[1])
#         elif(len(args)==3):
#             pre = '%s%d;3%d;4%d'%(pre,args[0],args[1],args[2])
#         pre = pre + 'm'
#         print(pre)
#     print(s)
#     print('\033[0m')
