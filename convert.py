import csv
import argparse
import enum

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('--final_balance')
    return parser.parse_args()

class OutputColumn(enum.Enum):
    DATE = 'Date'
    DESCRIPTION = 'Description'
    PAID_IN = 'Paid In'
    PAID_OUT = 'Paid Out'
    BALANCE = 'Balance'

    def __str__(self) -> str:
        return self.value

def convert(txn):
    return {
        OutputColumn.DATE: txn['Date'],
        OutputColumn.DESCRIPTION: f"{txn['Name'] + ' ' if txn['Name'] != '' else ''}{txn['Description']}",
        OutputColumn.PAID_IN: txn['Money In'],
        OutputColumn.PAID_OUT: txn['Money Out'].replace('-', ''),
        OutputColumn.BALANCE: ''
    }

if __name__ == '__main__':
    args = parse_args()
    with open(args.input_path) as input, open(args.input_path.replace('.csv', '.crunch.csv'), 'w') as output:
        txns = csv.DictReader(input)
        converted = [convert(txn) for txn in txns]
        converted[-1][OutputColumn.BALANCE] = args.final_balance or ''
        out = csv.DictWriter(output, [
            OutputColumn.DATE,
            OutputColumn.DESCRIPTION,
            OutputColumn.PAID_IN,
            OutputColumn.PAID_OUT,
            OutputColumn.BALANCE
        ])
        out.writeheader()
        out.writerows(converted)
