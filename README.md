# FASTA Reader & Sequence Analyzer

Этот проект представляет собой инструмент на Python для чтения и анализа биологических последовательностей в формате FASTA.

## Основные возможности:
- **Класс `Seq`**: хранит заголовок и последовательность, определяет длину и тип алфавита (нуклеотидный или белковый).
- **Класс `FastaReader`**: проверяет валидность файла и читает его по записям.
- **Оптимизация**: использование генераторов (`yield`) позволяет эффективно обрабатывать файлы любого размера, не перегружая оперативную память.

## Как запустить:
1. Укажите путь к вашему `.fasta` файлу в функции `demo()`.
2. Запустите скрипт: `python main.py`.

'''classDiagram
    class Seq {
        +String header
        +String sequence
        +__init__(header, sequence)
        +__str__() String
        +length() int
        +alphabet() String
    }
    class FastaReader {
        +is_fasta(filename) bool$
        +read(filename) Generator~Seq~
    }
    FastaReader ..> Seq : создает экземпляры'''
