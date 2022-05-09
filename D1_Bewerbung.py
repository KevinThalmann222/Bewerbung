class SoftwareIntegrationEngineer:
    def __init__(self, name: str, city: str, street: str, email: str, tel: str) -> None:
        self.name = name
        self.city = city
        self.street = street
        self.email = email
        self.tel = tel

    def requirements_software_tools(self) -> int:
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
            "knowledge_autosar": False,
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

    def print_cover_letter(self) -> None:
        """print the cover_letter"""
        print(
            f"{self.name} \n{self.city} \n{self.street} \n{self.email}\n"
            f"Tel.: {self.tel}\n"
            "\nBewerbung als 'Software Integration Engineer'\n"
            "\nSchönen guten Tag,\n"
            f"mein Name ist {self.name}"
            "und aus den folgenden drei Gründen glaube ich, "
            "dass ich Ihr Team im Bereich der Toolentwicklung nachhaltig "
            "verstärken und zu Ihrer Unternehmensstrategie beitragen kann."
            "\nPunkt 1:\n"
            "Ich bringe viele Ihrer Anforderungen bereits mit."
            "\nPunkt 2:\n"
            "Weiterhin profitieren Sie durch meine vertieften Kenntnisse im "
            "Bereich Softwareentwicklung im Bereich Toolchain-Entwicklung.\n"
            "In der Python-Umgebung fühle ich mich besonders wohl"
            "\nPunkt 3:\n"
            "Ebenfalls besonders interessant für Sie dürfte sein, dass ich "
            "sehr kreativ bin und bereits zahlreiche Ideen im internen "
            "Ideenspeicher der IAV verfasst habe. Auch Sie können von meiner "
            "Kreativität profitieren, denn die Mitgestaltung der "
            "Fahrzeugerlebnisse der Zukunft ist mir ein besonderes Anliegen.\n"
            "\nWas mich und Cariad verbindet, sind gemeinsame Werte, "
            "sowie zum Beispiel der Wunsch die Zukunft nachhaltig und "
            "innovativ zu gestalten und beim Kunden immer neue smarte "
            "Fahrerlebnisse zu erzeugen.\n"
            "Ihre beschriebene Stelle bietet mir dabei die Möglichkeit bei "
            "der Gestaltung der Zukunft mehr Verantwortung zu übernehmen als "
            "bislang und neue Konzepte zu entwickeln, denn im Zeitalter der "
            "Digitalisierung werden immer innovativere Lösungsansätze möglich "
            "sein. Mit meinen bisher gewonnenen Kenntnissen als "
            "Applikations-,sowie als Softwareentwickler im Bereich HIL "
            "Modeling und Toolchain-Entwicklung bringe ich bereits sehr viel "
            "benötigtes Knowhow im Bereich: "
            "Anforderungen/Änderungen/Fehlermanagement mit. Auch im "
            "Bereich der Bussysteme bringe ich Kenntnisse mit, um mit Ihnen "
            "die Innovation im Bereich autonome Fahrfunktionen "
            "weiterzubringen.\n"
            "In die für mich noch neuen Themengebiete wie Automotiv SPICE "
            "werde ich mich mit viel Ehrgeiz und der Bereitschaft Neues "
            "zu lernen einarbeiten.\n"
            "\nIch freue mich darauf, mit Ihnen im persönlichen Gespräch zu "
            "klären, wie ich Ihrem Team den größten Nutzen bringen kann.\n"
            "Lassen Sie uns die Zukunft gemeinsam gestalten.\n"
            "Liebe Grüße,\n"
            "\nKevin Thalmann"
        )


if __name__ == "__main__":
    application = SoftwareIntegrationEngineer(
        name="Kevin Thalmann",
        city="38106 Braunschweig",
        street="Spielmannstraße 16A",
        email="kevin_thalmann@yahoo.de",
        tel="015758485811",
    )
    score = application.requirements_software_tools()
    if score >= 80:
        application.print_cover_letter()
