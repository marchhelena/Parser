#-*- coding: utf-8 -*-
from lib import schedule_parser


if __name__ == "__main__":
    #при импорте не будет ниже реализовываться
    keywords = ("DATES", "COMPDAT", "COMPDATL")
    parameters = ()
    input_file = r"./input_data/test_schedule.inc"
    output_csv = "output_data/schedule.csv"

    schedule_df = schedule_parser.transform(keywords, parameters,
                                           input_file, output_csv)

print(input_file)