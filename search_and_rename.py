import os
import shutil


def search_for(path, filetype, dest):#这里需要传入文件夹的路径，以及需要移动的文件类型
    """
    函数输入:1.目标文件夹（如path=r"c:/"）；2.文件类型（如filepath=mp4）
    函数输出：复制目标文件至指定文件夹
    注意事项：需要提前定义输出的文件夹路径（如dest = r"I:\10.11 资源库-130条\学生作业-传资源库\重命名"）。
    简介：该函数用于搜寻目标文件夹，指定类型的文件。需要传入目标文件夹的路径以及搜索的文件类型，如path=r"c:/",filepath=mp4，这里
    需要提前定义输出的文件夹路径。
    """

    if os.path.isfile(path):#判断传输路径是否是文件，是文件路径，直接结束程序
        return
    else:
        del_file_in_dir(dest)
        path_list = os.listdir(path)#如果路径是文件夹，那列出该路径下的文件名（包括文件夹名）
        for item in path_list:#循环遍历，每一个文件名
            # print(item)
            path_item = os.path.join(path, item)#拼合成一个完整路径
            if os.path.isfile(path_item):#如果遍历对象是文件
                if path_item.endswith(filetype):#判断文件是否是txt文档或者mp4文档，并存到list中
                    list1.append(path_item)
                    shutil.copy(path_item, dest)#利用shutil模块，拷贝目标文件至相应的文件夹
                    continue
            if os.path.isdir(path_item):
                search_for(path_item, filetype)


def del_file_in_dir(dest):
    """
    函数输入：目标文件夹
    函数输出：删除文件夹下所有文件
    简介：查看文件夹内有无文件，如果有文件全部删除
    """
    os.chdir(dest)
    ls = os.listdir(dest)
    if ls != 0:
        for i in ls:
            c_path = os.path.join(dest, i)
            if os.path.isdir(c_path):
                del_file_in_dir(c_path)
            else:
                os.remove(c_path)


def file_rename(Ftype, author, course, dest):
    """
    函数输入：1.重命名文件类型（如Ftype="视频"）；2.作者名（如author = "zyl"）；3.课程名（如course = "运输包装实训"）；
            4.目标文件夹（est = r"c:/"）
    函数输出：目标文件夹内文件按照规律重命名，（如视频-运输包装实训1-zyl.mp4）
    简介：该函数用于重命名目标文件夹内的文件，该函数与上面的search_for必须连用使用时候需要传入改名信息.
        Ftype为视频的类型，author为视频的作者标识，dest为需要重命名的文件夹的路径。
        示例：Ftype="视频",author = "zyl",course = "运输包装实训"，dest = r"c:/"  结果为”视频-运输包装实训1-zyl.mp4“
    """

    os.chdir(dest) #更改工作路径，因为改名的文件与程序文件不在同一个目录
    temp_dir = os.listdir(dest) #列出目标文件夹下所有的文件
    for idx, item in enumerate(temp_dir, 1):#遍历所有文件，利用enumerate取出文件以及索引
        suffix = os.path.splitext(item)[-1]  # 分离得到文件后缀名（如.mp4），便于后续的rename操作。避免手工指定改名的文件类型
        with open("改名信息.txt", "a") as f: #记录改名的信息，方便查阅
            f.write(f"原文件名：{item}---->更改为：{Ftype}-{course}{idx}-{author}{suffix}\n")
        os.rename(item, f"{Ftype}-{course}{idx}-{author}{suffix}") #利用rename更改文件名



if __name__ == "__main__":
    list1 = []
    dest = r"C:\Users\GK\Desktop\dest1"
    search_for(r"C:\Users\GK\Desktop\test1", "pdf", dest)
    file_rename("视频", "zyl", "3d打印在包装中的应用", dest)