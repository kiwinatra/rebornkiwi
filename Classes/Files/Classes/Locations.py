import csv


class Locations:
    def getAllMaps():
        Maps = []
        with open('Classes/Files/assets/csv_logic/locations.csv', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[1].lower() != 'true':
                        Maps.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1
            return Maps

    def getMapsByMode(modeName):
        """Возвращает список ID карт (индексы locations.csv) для указанного режима,
        исключая disabled и служебные."""
        Maps = []
        excluded_names = {"PlayerMapTemplate", "Tutorial", "Training", "SurvivalTutorial"}
        with open('Classes/Files/assets/csv_logic/locations.csv', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    name = row[0]
                    disabled = row[1].lower() == 'true'
                    mode = row[7]
                    if not disabled and mode == modeName and name not in excluded_names:
                        Maps.append(line_count - 2)
                    if name != "":
                        line_count += 1
        return Maps
