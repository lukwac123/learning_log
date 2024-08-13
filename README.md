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




