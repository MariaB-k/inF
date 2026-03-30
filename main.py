class Seq:
    """Класс для хранения и анализа биологической последовательности."""
    
    def __init__(self, header, sequence):
        """Инициализация объекта Seq."""
        self.header = header  # заголовок FASTA‑записи (строка после >)
        self.sequence = sequence  # биологическая последовательность

    def __str__(self):
        """Возвращает строку в формате FASTA."""
        # красивое строковое представление
        return f">{self.header}\n{self.sequence}"  # возврат строки в формате FASTA

    def length(self):
        """Возвращает длину последовательности."""
        # длина последовательности
        return len(self.sequence)

    def alphabet(self):
        """Определяет алфавит последовательности."""
        # определяем алфавит: нуклеотидный или белковый
        nucleotides = set('ATCGU')
        proteins = set('ACDEFGHIKLMNPQRSTVWY')
        seq_set = set(self.sequence)

        if not seq_set:
            return "неизвестный (пустая последовательность)"
        elif seq_set.issubset(nucleotides):
            return "нуклеотидный"
        elif seq_set.issubset(proteins):
            return "белковый"
        else:
            return "неизвестный"

class FastaReader:
    """Класс для чтения FASTA файлов с проверкой формата."""
    
    @staticmethod
    def is_fasta(filename):
        """Проверяет, является ли файл форматом FASTA."""
        try:
            with open(filename, 'r') as f:
                first_line = f.readline().strip()
                return first_line.startswith('>')
        except:
            return False

    def read(self, filename):
        """Генератор для чтения записей из файла по одной."""
        if not self.is_fasta(filename):
            raise ValueError("Файл не в формате FASTA")

        with open(filename, 'r') as f:
            header = None
            sequence = []

            for line in f:
                line = line.strip()
                if not line:
                    continue

                if line.startswith('>'):
                    if header is not None:
                        yield Seq(header, ''.join(sequence))
                    header = line[1:]  # сохраняем заголовок без '>'
                    sequence = []  # очищаем список для новой последовательности
                else:  # правильно привязанный else к if line.startswith('>')
                    sequence.append(line)  # добавляем строку последовательности

            # выдаём последнюю запись после завершения цикла
            if header is not None:
                yield Seq(header, ''.join(sequence))

def demo():
    """Запуск демонстрации работы программы."""
    reader = FastaReader()
    filename = "/Users/mariabrik/Downloads/sequence.fasta"

    if reader.is_fasta(filename):
        print("Файл соответствует формату FASTA")
        for seq in reader.read(filename):
            print(seq)
            print(f"Длина: {seq.length()}")
            print(f"Алфавит: {seq.alphabet()}")
    else:
        print("Файл не в формате FASTA")

if __name__ == "__main__":
    demo()


