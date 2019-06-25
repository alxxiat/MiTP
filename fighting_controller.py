def fight_controller(attacker, target, attacktype):
    if attack_type == "physical":
        target.stats["health"] -= attacker.stats["strength"]
        print(repr(attacker) + " attacked " + repr(target) + "with" +
              str(attacker.stats["strength"]) + " power")
    if attack_type == "magical":
        target.stats["health"] -= attacker.stats["magicpower"]
        print(repr(attacker) + " attacked " + repr(target) + "with" +
              str(attacker.stats["magicpower"]) + " power")