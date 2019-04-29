#coding=utf-8
import commands
def create_db():
    #lmdb文件名字
    lmdb_name = 'img_test.lmdb'
    #生成的db文件的保存目录
    lmdb_save_path ='/mnt/hgfs/share_vmware/classfy/' + lmdb_name
    txt_save_path ='/mnt/hgfs/share_vmware/classfy/labelTest.txt'
    images_path ='/mnt/hgfs/share_vmware/classfy/testset/'
    #convert_imageset工具路径
    convert_imageset_path = "~/Documents/caffe/" + 'build/tools/convert_imageset'
    cmd = """%s --shuffle --resize_height=256 --resize_width=256 %s %s %s"""
    status, output = commands.getstatusoutput(cmd % (convert_imageset_path, images_path, 
        txt_save_path, lmdb_save_path))
    print output
    if(status == 0):
        print "lmbd文件生成成功"
create_db()