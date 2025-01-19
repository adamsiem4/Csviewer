# Dokumentacja Projektu: "Przeglądarka CSV i Sortowanie" (oparta o SAFe® 6.0)

## 1. Wprowadzenie
Celem tego projektu jest stworzenie aplikacji do przeglądania i sortowania danych z plików CSV, z interfejsem graficznym zaprojektowanym w Pythonie z wykorzystaniem biblioteki Tkinter. Projekt jest zgodny z wytycznymi SAFe® 6.0 i przyjmuje podejście iteracyjne, umożliwiające regularne dostarczanie wartości dla interesariuszy.

---

## 2. Wizja Produktu

Aplikacja umożliwia użytkownikom:

- Wyświetlanie danych z plików CSV w przyjaznym interfejsie graficznym.
- Sortowanie danych według wybranych kolumn.
- Pracę w trybie ciemnego motywu (dark mode), poprawiając komfort pracy.
- Przeglądanie ograniczonych wyników (pierwsze 100 rekordów) w celu optymalizacji wydajności.

---

## 3. Cel Biznesowy

Projekt ma na celu wsparcie operacji analizy danych przez dostarczenie łatwego w obsłudze narzędzia umożliwiającego szybkie i efektywne przeglądanie oraz sortowanie danych CSV.

---

## 4. Kluczowe Funkcjonalności

### 4.1 Wczytywanie Plików CSV

- Automatyczne ładowanie danych z pliku CSV zdefiniowanego w kodzie.
- Obsługa błędów podczas ładowania danych.

### 4.2 Wyświetlanie Danych

- Interfejs oparty na kontrolce `Treeview` z paskami przewijania (pionowym i poziomym).
- Limit wyników do 100 rekordów, aby zapewnić płynne działanie aplikacji.

### 4.3 Sortowanie

- Użytkownik może sortować dane według wybranej kolumny w porządku rosnącym lub malejącym.

### 4.4 Interfejs Użytkownika

- Tryb ciemny (dark mode) dla lepszej czytelności i komfortu pracy.
- Responsywność interfejsu w pełnym oknie aplikacji.

---

## 5. Realizacja Wartości w SAFe

### 5.1 ART (Agile Release Train)

Ten projekt jest częścią inicjatywy Agile Release Train, skupiającej się na aplikacjach analitycznych. Kluczowym celem jest poprawa produktywności analityków danych poprzez uproszczenie ich codziennych zadań.

### 5.2 Epiki

- **Epik 1**: Stworzenie interfejsu graficznego dla aplikacji.
- **Epik 2**: Dodanie funkcji sortowania danych.
- **Epik 3**: Implementacja trybu ciemnego.
- **Epik 4**: Optymalizacja wydajności dla dużych plików CSV.

### 5.3 Funkcje

Każdy epik został podzielony na mniejsze funkcje realizowane podczas iteracji:

- Wyświetlanie danych w tabeli.
- Obsługa pasków przewijania.
- Dodanie przycisków sortowania i ich logiki.

### 5.4 Iteracje

Projekt jest realizowany w podejściu iteracyjnym:

- **Iteracja 1**: Wyświetlenie danych w tabeli z podstawową funkcjonalnością.
- **Iteracja 2**: Dodanie sortowania danych.
- **Iteracja 3**: Wprowadzenie trybu ciemnego i optymalizacja wizualna.

---

## 6. Techniczne Szczegóły

### 6.1 Technologia

- **Język programowania**: Python 3
- **Biblioteki**: pandas, tkinter

### 6.2 Struktura Kodowa

- **`load_csv(file_path)`**: Funkcja ładująca dane z pliku CSV.
- **`display_data(data, tree)`**: Funkcja wyświetlająca dane w widoku Treeview.
- **`sort_data(data, tree, sort_column, ascending)`**: Funkcja implementująca sortowanie danych.
- **Główna funkcja `main()`**: Obsługa interfejsu graficznego i logiki aplikacji.

### 6.3 Optymalizacja

- Ograniczenie wyników do 100 rekordów.
- Dodanie pasków przewijania.

---

## 7. Testowanie

### 7.1 Testy Manualne

1. Wczytanie pliku CSV i sprawdzenie poprawności danych.
2. Przetestowanie sortowania danych dla każdej kolumny.
3. Walidacja interfejsu użytkownika (czytelność, responsywność).

### 7.2 Testy Automatyczne

- Testy jednostkowe dla funkcji sortujących.
- Testy dla poprawności ładowania danych CSV.

---

## 8. Wymagania Niefunkcjonalne

- Aplikacja powinna działać w systemach Windows, macOS i Linux.
- Czas reakcji aplikacji podczas sortowania nie powinien przekraczać 2 sekund dla 100 rekordów.

---

## 9. Potencjalny Rozwój

- Dodanie obsługi filtrowania danych.
- Eksport wyników sortowania do nowego pliku CSV.
- Integracja z bazami danych (np. MySQL, PostgreSQL).
- Responsywny interfejs webowy jako alternatywa dla aplikacji desktopowej.

---

## 10. Podsumowanie

Projekt "Przeglądarka CSV i Sortowanie" realizuje założenia SAFe® 6.0 poprzez iteracyjne podejście do budowy funkcjonalnego narzędzia analitycznego. Dzięki optymalizacji wydajności i przyjaznemu interfejsowi, aplikacja jest wartościowym wsparciem dla analityków danych i innych użytkowników.

