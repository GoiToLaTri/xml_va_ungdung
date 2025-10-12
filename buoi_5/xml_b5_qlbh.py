from lxml import etree

tree = etree.parse('quanlybanan.xml')

"""#### **Lấy tất cả bàn**"""

all_table = tree.xpath('//BAN/SOBAN/text() | //BAN/TENBAN/text()')
print(all_table)

"""#### **Lấy tất cả nhân viên**"""

all_staff = tree.xpath('//NHANVIEN/TENV/text()')
print(all_staff)

"""#### **Lấy tất cả tên món**"""

all_dish = tree.xpath('//MON/TENMON/text()')
print(all_dish)

"""#### **Lấy tên nhân viên có mã NV02**"""

name_of_nv02 = tree.xpath('//NHANVIEN[MANV="NV02"]/TENV/text()')
print(name_of_nv02)

"""#### **Lấy tên và số điện thoại của nhân viên NV03**"""

nv_03_name_phone = tree.xpath('//NHANVIEN[MANV="NV03"]/TENV/text() | //NHANVIEN[MANV="NV03"]/SDT/text()')
print(nv_03_name_phone)

"""#### **Lấy tên món có giá > 50,000**"""

dish_more_than_50k = tree.xpath('//MON[GIA > 50000]/TENMON/text()')
print(dish_more_than_50k)

"""#### **Lấy số bàn của hóa đơn HD03**"""

hb03_table = tree.xpath('//HOADON[SOHD="HD03"]/SOBAN/text()')
print(hb03_table)

"""#### **Lấy tên món có mã M02**"""

dish_m02 = tree.xpath('//MON[MAMON="M02"]/TENMON/text()')
print(dish_m02)

"""#### **Lấy ngày lập của hóa đơn HD03**"""

create_at_hd03 = tree.xpath('//HOADON[SOHD="HD03"]/NGAYLAP/text()')
print(create_at_hd03)

"""#### **Lấy tất cả mã món trong hóa đơn HD01**"""

all_id_dish_hd01 = tree.xpath('//HOADON[SOHD="HD01"]/CTHDS/CTHD/MAMON/text()')
print(all_id_dish_hd01)

"""#### **Lấy tên món trong hóa đơn HD01**"""

all_name_dish_hd01 = tree.xpath("//MON[MAMON=//HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON]/TENMON/text()")
print(all_name_dish_hd01)

"""#### **Lấy tên nhân viên lập hóa đơn HD02**"""

name_nv_cre_hd02 = tree.xpath("//NHANVIEN[MANV=//HOADON[SOHD='HD02']/MANV/text()]/TENV/text()")
print(name_nv_cre_hd02)

"""#### **Đếm số bàn**"""

total_table = tree.xpath('count(//BAN)')
print(total_table)

"""#### **Đếm số hóa đơn lập bởi NV01**"""

invoice_creted_by_nv01 = tree.xpath('count(//HOADON[MANV="NV01"])')
print(invoice_creted_by_nv01)

"""#### **Lấy tên tất cả món có trong hóa đơn của bàn số 2**"""

name_of_dish_in_table_2 = tree.xpath("//MON[MAMON=//HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]/TENMON/text()")
print(name_of_dish_in_table_2)

"""#### **Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3**"""

table_3_nv = tree.xpath("//NHANVIEN[MANV=//HOADON[SOBAN='3']/MANV/text()]/TENV/text()")
print(table_3_nv)

"""#### **Lấy tất cả hóa đơn mà nhân viên nữ lập**"""

all_invoice_cre_by_female = tree.xpath("//HOADON[MANV=//NHANVIEN[GIOITINH='Nữ']/MANV]/SOHD/text()")
print(all_invoice_cre_by_female)

"""#### **Lấy tất cả nhân viên từng phục vụ bàn số 1**"""

all_staff_table01 = tree.xpath("//NHANVIEN[MANV=//HOADON[SOBAN='1']/MANV/text()]/TENV/text()")
print(all_staff_table01)

"""#### **Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn**"""

dish_more_than_1_time = tree.xpath("//MON[MAMON=//HOADON/CTHDS/CTHD[SOLUONG>1]/MAMON]/TENMON/text()")
print(dish_more_than_1_time)

"""#### **Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'**"""

table_and_cre_at_of_hd02 = tree.xpath("//BAN[SOBAN=//HOADON[SOHD='HD02']/SOBAN]/TENBAN/text() | //HOADON[SOHD='HD02']/NGAYLAP/text()")
print(table_and_cre_at_of_hd02)