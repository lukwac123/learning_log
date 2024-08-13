# Projekt aplikacji internetowej z użyciem framework'a Django oraz nadanie stylu z użyciem biblioteki Bootstrap.

## Specyfikacja projektu.

Utworzenie aplikacji internetowej o nazwie [**_Learning Log_**](https://main-bvxea6i-mfi522clqjnxe.us-3.platformsh.site/), 
która pozwala użytkownikom zapisywać interesujące ich tematy oraz dodawać wpisy do dziennika podczas poznawania danego zagadnienia.

Strona główna aplikacji zawiera opis wyjaśniający przeznaczenie tej witryny internetowej oraz zachęca do użytkowników
do zarejestrowania się lub zalogowania. Po zalogowaniu każdy użytkownik ma możliwość utworzenia nowego tematu, 
dodania nowego wpisu, a także odczytania i edytowania istniejących wpisów.

Kiedy poznaje się nowe zagadnienie, prowadzenie dziennika, w którym można zapisywać to czego się już nauczyło, może
być pomocne w monitorowaniu postępów oraz podczas ponownego przeglądania zebranych informacji. Dzięki takiej aplikacji
jak [**_Learning Log_**](https://main-bvxea6i-mfi522clqjnxe.us-3.platformsh.site/) ten proces może być znaczenie bardziej efektywny.

![main_site](https://github.com/user-attachments/assets/b5edd5e2-12c1-41be-957b-43cb6227ddc3)

<sup>Rys.1 Strona główna aplikacji Learning Log</sup>

## 1. Przygotowanie projektu.

### 1.1 Utworzenie środowiska wirtualnego.
Do pracy z Django potrzebne jest skonfigurowanie środowiska wirtualnego, czyli miejsca w systemie, w którym można instalować
pakiety i odizolować je od pozostałych pakietów. W powłoce przechodzimy do nowo utworzonego katalogu _learning_log_ i tworzymy 
w nim środowisko wirtualne za pomocą polecenia:
```
learning_log$ python -m venv ll_env
```
### 1.2 Aktywacja środowiska wirtualnego.
Aktywacji dokonujemy za pomocą polecenia:
```
learning_log$ ll_env\Scripts\activate
(ll_env)learning_log$
```
Środowisko wirtualne jest aktywne wtedy jeżeli jego nazwa będzie wyświetlana w nawiasie (), przed znakiem zachęty w powłoce.
Aby zakończyć działanie środowiska wirtualnego należy wydać poniższe polecenie lub zamknąć okno powłoki, które było aktywne:
```
(ll_env)learning_log$ deactivate
learning_log$ 
```
## 1.3 Instalacja framework'a Django.
W aktywnym środowisku wirtualnym w pierwszej kolejności aktualizujemy narzędzie pip do pobierania pakietów, a następnie
używając kolejnego polecenia instalujemy framework Django:
```
(ll_env)learning_log pip install --upgrade pip
(ll_env)learning_log pip install django
```
## 1.4 Utworzenie projektu w Django
Mając aktywne środowisko wirtualne tworzymy projekt używając poniższego polecenia:
```
(ll_env)learning_log$ django-admin statrproject ll_project .
```
Polecenie _startproject_ nakazuje Django utworzenie nowego projektu o nazwie _ll_project_ wraz z odpowiednią strukturą katalogów.
## 1.5 Utworzenie bazy danych.
Większość informacji w projekcie przechowywana jest w bazie danych, tak więc kolejnym krokiem jest jej utowrzenie, wykonujemy to
przy pomocy poniższego polecenia:
```
(ll_env)learning_log$ python manage.py migrate
```
Wydanie polecenia pierwszy raz powoduje że Django utworzy bazę danych, następnie po każdorazowej modyfikacji bazy danych powyższe
polecenie powoduje że jest ona aktualizowana.

## 1.6 Przegląd projektu.
Aby sprawdzić poprawność przygotowanego projektu należy wydać polecenie:
```
(ll_env)learning_log$ python manage.py runserver
```
Jeżeli wszystko zostało wykonane poprawnie, otwierając przeglądarkę stron internetowych i wybierając adres URL: ```http://localhost:8000/``` lub ```http://127.0.0.1:8000/```
powinien pojawić się ekran startowy framework'a Django z informacją że instalacja jego przebiegła pomyślnie.





