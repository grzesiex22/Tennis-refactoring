# Tennis Refactoring Kata in Python

## Zmiany

- Zastosowano jednoznaczne, opisowe nazwy zmiennych i argumentów (np. `player1_points` zamiast `p1`), co znacząco zwiększyło czytelność kodu.
- Uogólniono warunek w funkcji `won_point` — zamiast porównywania z zahardkodowaną nazwą `"player1"`, porównanie odbywa się dynamicznie względem nazw przekazanych w konstruktorze.
- Zmieniono nieczytelną konstrukcję `(x - y) * (x - y) == 1` na bardziej przejrzyste `abs(x - y) == 1`.
- Rozbito złożoną logikę funkcji `score()` na mniejsze metody pomocnicze:
  - `_is_early_game()` — sprawdza, czy gra jest w początkowej fazie (przed "Deuce"),
  - `_early_score()` — zwraca wynik w fazie początkowej,
  - `_endgame_score()` — obsługuje przypadki "Advantage" i "Win".
- Dzięki rozdzieleniu logiki kod jest bardziej czytelny, modularny i łatwiejszy do testowania.
- Zastąpiono złożone wyrażenia warunkowe z operatorami warunkowymi (`if ... else`) osobnymi instrukcjami `if` z `return`, co poprawia przejrzystość.

