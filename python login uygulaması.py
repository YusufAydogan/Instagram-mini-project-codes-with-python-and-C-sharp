While True:
  sysUserName = "yusuf"
  sysUserPassword = "123456"
  
  print("")
  userName = input("Kullanıcı adınızı giriniz: ")
  userPassword = input("Şifrenizi giriniz: ")
  
  if userName == sysUserName and userPassword == sysPassword:
    print("Bilgiler doğru, uygulamaya giriş yapılıyor...")
    break
  elif userName != sysUserName and userPassword == sysUserPassword:
    print("Kullanıcı adı yanlış lütfen tekrar deneyiniz...")
  elif userName == sysUserName and userPassword != sysUserPassword:
    print("Şifreniz yanlış lütfen tekrar deneyiniz...")
  else:
    print("Kullanıcı adı ve şifre yanlış lütfen tekrar deneyiniz...")
