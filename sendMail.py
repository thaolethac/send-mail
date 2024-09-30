import yagmail
def sendMail(toMail, name, isPassed):
    
    if(isPassed):
        yag = yagmail.SMTP("bit.mis@bav.edu.vn", "mytb judm wmaz spva")

        subject = "THÔNG BÁO KẾT QUẢ VÒNG ĐƠN TUYỂN CTV GEN 15 CLB TIN HỌC NGÂN HÀNG BIT - BAV"
        body = '''
    Thân gửi bạn <strong>{name}</strong>,<br>
      Lời đầu tiên, <strong>CLB Tin học Ngân hàng BIT - BAV</strong> xin gửi lời cảm ơn tới bạn vì đã dành thời gian và sự quan tâm đến chương trình <strong>TUYỂN CỘNG TÁC VIÊN GEN 15</strong> của <strong>BIT</strong>. Thông qua hai vòng tuyển chọn vừa qua, <strong>BIT</strong> xin trân trọng thông báo:
    <h3 style="color: blue; text-align: center">
      CHÚC MỪNG BẠN ĐÃ CHÍNH THỨC TRỞ THÀNH MỘT MẢNH GHÉP CỦA CLB TIN HỌC NGÂN HÀNG BIT - BAV
    </h3>
      Bạn đã thể hiện rất xuất sắc trong vòng phỏng vấn vừa qua và ngày hôm nay <strong>BIT</strong> xin chúc mừng bạn với vai trò là <strong>CTV CLB Tin học Ngân hàng BIT - BAV</strong>. Hy vọng chặng đường sắp tới bạn sẽ cùng <strong>CLB Tin học Ngân hàng BIT - BAV</strong> gặt hái được nhiều thành công và có thật nhiều kỷ niệm đẹp cùng nhau để những năm tháng đại học của bạn sẽ là đoạn ký ức tươi đẹp nhất.<br>
      Bạn hãy tham gia link mess dưới đây để cùng vào đại gia đình <strong>CLB Tin học Ngân hàng BIT - BAV</strong> nhé: <a href="https://m.me/j/AbY9GARcYvYK3GrC">https://m.me/j/AbY9GARcYvYK3GrC</a><br>
      <strong>BIT</strong> xin gửi bạn thông tin chi tiết về thời gian và địa điểm diễn ra buổi <strong>“First Meeting”</strong> cụ thể như sau:<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>1. Thời gian:</strong> 18h30 Thứ Tư, ngày 25/09/2024
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>2. Địa điểm:</strong> Tầng 3 Nhà E - Học viện Ngân hàng<br>
      <strong>BIT</strong> rất mong chờ sự hiện diện của bạn trong buổi <strong>Gặp mặt đầu năm</strong> để chúng mình có cơ hội giao lưu và hiểu nhau hơn nhé!<br>
    <strong>Trân trọng!</strong>
'''.format(name=name)
        yag.send(to=toMail, subject=subject, contents=body)
    else:
        yag = yagmail.SMTP("bit.mis@bav.edu.vn", "mytb judm wmaz spva")

        subject = "THÔNG BÁO KẾT QUẢ VÒNG ĐƠN TUYỂN CTV GEN 15 CLB TIN HỌC NGÂN HÀNG BIT - BAV"
        body = '''
    Thân gửi bạn <strong>{name}</strong>,<br>
      Lời đầu tiên, <strong>CLB Tin học Ngân hàng BIT - BAV</strong> xin gửi lời cảm ơn tới bạn vì đã dành thời gian và sự quan tâm đến chương trình <strong>TUYỂN CỘNG TÁC VIÊN GEN 15</strong> của <strong>BIT</strong>. Thông qua hai vòng tuyển chọn vừa qua, <strong>BIT</strong> xin trân trọng thông báo:<br>
      Sau khi xem xét kỹ lưỡng hồ sơ và đánh giá quá trình phỏng vấn, rất tiếc chúng mình chưa thể chọn bạn vào <strong>Câu lạc bộ</strong> đợt này.<br>
      Chúng mình rất trân trọng những nỗ lực và sự nhiệt huyết của bạn. Tuy nhiên, do số lượng ứng viên đông đảo và tiêu chí chọn lọc kỹ lưỡng, chúng mình đành phải đưa ra quyết định này. Dù vậy, chúng mình tin rằng bạn có nhiều tiềm năng phát triển và mong rằng bạn sẽ tiếp tục giữ tinh thần nhiệt huyết, không ngừng rèn luyện bản thân.<br>
      Hy vọng trong tương lai, bạn sẽ có cơ hội khác để tham gia và đồng hành cùng chúng mình. Chúc bạn thật nhiều may mắn và thành công trong những dự định sắp tới!<br>
    <strong>Trân trọng!</strong>
    '''.format(name=name)
        yag.send(to=toMail, subject=subject, contents=body)
    
    
