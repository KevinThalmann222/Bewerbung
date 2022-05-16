from pathlib import Path


class SimulationSoftwareEngineer:
    """Bitte Funktion ausführen, es wird eine .txt erzeugt.

    liebe Grüße,
    Kevin Thalmann
    """

    def __init__(self, name: str, city: str, street: str, email: str, tel: str, job: str, team: str) -> None:
        self.name = name
        self.city = city
        self.street = street
        self.email = email
        self.tel = tel
        self.job = job
        self.team = team

    def job_requirements(self) -> int:
        """calculates the match of the requirements in percent

        Returns:
            int: score in percent
        """
        requirements_dic = {
            "degree_vehicle_engineering": True,
            "jira_skills": True,
            "coding_languages_python": True,  # very good
            "coding_languages_matlab": True,  # good
            "coding_languages_c": False,  # a little bit
            "ci_cd_experience": True,  # course at october
            "car_maker": False,  # a little bit
            "communication_skills": True,
            "creativity": True,
            "communicative": True,
        }
        accordance = []
        for key, value in requirements_dic.items():
            if value:
                accordance.append(key)
        score = int(len(accordance) / len(requirements_dic) * 100)

        return score

    def print_cover_letter(self) -> str:
        """print the cover_letter"""
        cover_letter = (
            f"{self.name} \n{self.city} \n{self.street} \n{self.email}\n"
            f"Tel.: {self.tel}\n"
            f"\nBewerbung als '{self.job}'\n"
            "\nSchönen guten Tag,\n"
            f"\nmein Name ist {self.name}"
            "und aus den folgenden drei Gründen glaube ich,\n"
            f"dass ich Ihr Team im Bereich der {self.team} nachhaltig\n"
            "verstärken und zu Ihrer Unternehmensstrategie beitragen kann.\n"
            "\nPunkt 1:\n"
            "Mit meinem Hintergrund als Applikationsingenieur, "
            "bringe ich Erfahrungen im Erstellen von Lastenheften\n"
            "sowie in der Entwicklung, Applikation, Absicherung und "
            "Testen von komplexen Systemen mit."
            "\nPunkt 2:\n"
            "Weiterhin profitieren Sie durch meine vertieften Kenntnisse "
            "im Bereich Softwareentwicklung,\n"
            "die ich in meiner aktuellen "
            "Tätigkeit als Softwareentwickler gewinnen konnte.\n"
            "Hierzu zählen unter anderem, dass Programmieren "
            "und Testen von Funktionen zur Automatisierung "
            "von HIL-Modellierungstätigkeiten"
            "\nPunkt 3:\n"
            "Ebenfalls besonders interessant für Sie dürfte sein, dass ich "
            "sehr kreativ bin und bereits zahlreiche Ideen im internen "
            "Ideenspeicher der IAV verfasst habe."
            "\nAuch Sie können von meiner "
            "Kreativität profitieren, denn die Mitgestaltung der "
            "Fahrzeugerlebnisse der Zukunft ist mir ein besonderes Anliegen.\n"
            "\nWas mich und Cariad verbindet, sind gemeinsame Werte, "
            "sowie zum Beispiel der Wunsch die Zukunft nachhaltig und\n"
            "innovativ zu gestalten und beim Kunden immer neue smarte "
            "Fahrerlebnisse zu erzeugen.\n"
            "Ihre beschriebene Stelle bietet mir dabei die Möglichkeit bei "
            "der Gestaltung der Zukunft mehr Verantwortung zu übernehmen als "
            "bislang und neue Konzepte zu entwickeln,\n"
            "denn im Zeitalter der Digitalisierung werden immer innovativere "
            "Lösungsansätze möglich sein.\n"
            "\nMit meinen bisher gewonnenen Kenntnissen als Applikations-, "
            "sowie als Softwareentwickler bringe ich bereits sehr viel "
            "benötigtes Knowhow im Konzeptionieren, Koordinieren und \n"
            "Spezifizieren von System- und Komponentenanforderungen, "
            "Ausarbeitung von Software-Freigabe-Empfehlungen, "
            "in der Entwicklung und Programmierung von Funktionen\n"
            "(in Python und Matlab), sowie schreiben "
            "und durchführen von Unit-Tests mit.\n"
            "\nIn die für mich noch neuen Themengebiete wie "
            "C/C ++ werde ich mich mit viel Ehrgeiz "
            "und der Bereitschaft Neues zu lernen einarbeiten.\n"
            "\nZu meinen größten Erfolgen zählt die Entwicklung "
            "eines Prozesses zur Testcase-Automatisierung am Gesamtfahrzeug "
            ", welcher es erlaubt Erprobungen auch remote durchzuführen.\n"
            "Hierfür wurde ein Budget von 10.000 Euro zu Verfügung gestellt.\n"
            "\nIch freue mich darauf, mit Ihnen im persönlichen Gespräch zu "
            "klären, wie ich Ihrem Team den größten Nutzen bringen kann.\n"
            "Lassen Sie uns die Zukunft gemeinsam gestalten.\n"
            "\nFür mehr Infomationen zu mir und meinem Lebenslauf "
            "besuchen Sie mich gerne hier: \n"
            "\nhttps://kevinthalmann222.github.io/\n"
            "\nLiebe Grüße,\n"
            "Kevin Thalmann\n"
        )
        print(cover_letter)

        return cover_letter

    def export_cover_letter(self) -> None:
        """Schreibt die Bewerbung in eine .txt Datei"""
        with open(Path(__file__).parent / "Bewerbung_KevinThalmann.txt", "w", newline="\n") as file:
            file.write(self.print_cover_letter())


if __name__ == "__main__":
    application = SimulationSoftwareEngineer(
        name="Kevin Thalmann",
        city="38106 Braunschweig",
        street="Spielmannstraße 16A",
        email="kevin_thalmann@yahoo.de",
        tel="015758485811",
        job="Simulation Software Engineer",
        team="Predictive Safety",
    )
    score = application.job_requirements()
    print(f"score = {score}%")
    print("-" * 20)
    if score >= 80:
        application.print_cover_letter()
    application.export_cover_letter()
