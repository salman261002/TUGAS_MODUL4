print('=======================================================')
print('              PROGRAM KUMPULAN APLIKASI                ')
print('=======================================================')
print('')
print('Kelompok 6 DKP')
print('Nama Anggota: ')
print('1. Muhammad Salman Alfarisi - 21120120120001')
print('2. ')
print('3. ')
print('4. Rina Santika - 21120120120030')
print('=======================================================')
print('')
print('=======================================================')

import modulgbk ,smtplib ,ssl

def funcemail():
    emailpengirim=input('Masukkan email kamu!: ')
    password = input('Masukkan password kamu!: ')
    emailpenerima=input('Masukkan email tujuan!: ')
    subjek=input('Masukkan subjek email!: ')
    pesan=input('Masukkan pesan kamu!: ')
    print('=======================================================')

    message='''Subject: {0}

    {1}'''.format(subjek ,pesan)

    port = 465  # For SSL

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(emailpengirim, password)
        server.sendmail(emailpengirim, emailpenerima, message)

    print('Email terkirim!')
    print('=======================================================')

    #pengulangan
pengulangan='yes'
while pengulangan=='yes':
    print('Daftar aplikasi: ')
    print('1. Gunting Kertas Batu')
    print('2. Aplikasi Pengirim Email')
    print('=======================================================')
    nomorgame=int(input('Pilih game yang kamu mau!: '))
    print('=======================================================')

    #pengondisian
    if nomorgame==1:
        main1=modulgbk.play()
    elif nomorgame==2:
        funcemail()
    ulang=input('Ulangi program?(y/n): ')
    if ulang =='y':
        pengulangan='yes'
        print('=======================================================')
    else:
        print('=======================================================')
        print('Program telah selesai!')
        print('Terimakasih!')
        print('=======================================================')
        break
    
