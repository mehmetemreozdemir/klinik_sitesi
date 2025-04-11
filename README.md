# Klinik Sitesi

Bu proje, modern bir klinik web sitesi uygulamasıdır. Frontend ve backend bileşenlerini içerir.

## Özellikler

- Randevu sistemi
- Blog yönetimi
- Doktor profilleri
- Hizmet bilgileri
- İletişim formu

## Teknolojiler

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Django
- SQLite

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/mehmetemreozdemir/klinik_sitesi.git
cd klinik_sitesi
```

2. Backend kurulumu:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

3. Frontend'i tarayıcıda açın:
- `frontend/index.html` dosyasını bir web tarayıcısında açın

## Katkıda Bulunma

1. Bu depoyu forklayın
2. Yeni bir özellik dalı oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Dalınıza push yapın (`git push origin yeni-ozellik`)
5. Bir Pull Request oluşturun# klinik_sitesi
