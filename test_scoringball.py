# Manba Xazratov Behro'z
from TournamentScoringSystem import TournamentScoringSystem
class TestTournamentScoringSystem:
    def __init__(self):
        self.system = TournamentScoringSystem()

    def test_player(self):
        print("=== ishtirokchilarni qo'shishni test qilamiz ===")
        self.system.player()

    def test_team(self):
        print("=== jamoalarni qo'shishni test qilamiz ===")
        self.system.team()

    def test_update_ball(self):
        print("=== ishtirokchining balini o'zgartirishni test qilamiz ===")
        self.system.updateBall()

    def test_overall_of_team(self):
        print("=== jamoalar umumiy ballarini test qilamiz ===")
        self.system.overallOfteam()

    def test_overall_of_player(self):
        print("=== ishtirokchilar umumiy ballarini test qilamiz ===")
        self.system.overallOfplayer()

    def test_overall(self):
        print("=== Shartlar va berilgan ballarni test qilamiz ===")
        self.system.overall()

    def test_message(self):
        print("=== Xat yo'llashni test qilamiz ===")
        self.system.message()

    def run_all_tests(self):
        self.test_player()
        self.test_team()
        self.test_update_ball()
        self.test_overall_of_team()
        self.test_overall_of_player()
        self.test_overall()
        self.test_message()

if __name__ == "__main__":
    tester = TestTournamentScoringSystem()
    tester.run_all_tests()
