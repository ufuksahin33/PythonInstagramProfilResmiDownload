import instaloader

ig = instaloader.Instaloader()
profile=input("Kullanıcı adı giriniz:")

ig.download_profile(profile, profile_pic_only=True)