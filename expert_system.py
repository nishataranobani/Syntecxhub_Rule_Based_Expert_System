# Rule-Based Expert System
# Syntecxhub Artificial Intelligence Internship - Project 2

class ExpertSystem:
    def __init__(self):
        # Fact base
        self.facts = set()

        # IF-THEN rules
        self.rules = [
            {
                "if": {"fever", "cough"},
                "then": "respiratory_infection"
            },
            {
                "if": {"respiratory_infection"},
                "then": "rest_and_hydration"
            },
            {
                "if": {"fever", "body_ache"},
                "then": "flu_like_symptoms"
            },
            {
                "if": {"flu_like_symptoms"},
                "then": "monitor_temperature"
            },
            {
                "if": {"respiratory_infection", "body_ache"},
                "then": "consult_doctor"
            },
            {
                "if": {"high_fever", "difficulty_breathing"},
                "then": "seek_medical_attention"
            }
        ]

        # Stores the reasoning process
        self.inference_log = []

    def add_fact(self, fact):
        """Add a new fact to the fact base."""
        self.facts.add(fact)

    def forward_chain(self):
        """Apply rules repeatedly until no new facts can be derived."""

        changed = True

        while changed:
            changed = False

            for rule in self.rules:
                conditions = rule["if"]
                conclusion = rule["then"]

                # Check whether all conditions are known facts
                if conditions.issubset(self.facts):
                    if conclusion not in self.facts:

                        # Add the new conclusion to the fact base
                        self.facts.add(conclusion)
                        changed = True

                        # Log the reasoning step
                        conditions_text = " AND ".join(sorted(conditions))

                        log_message = (
                            f"Rule applied: IF {conditions_text} "
                            f"THEN {conclusion}"
                        )

                        self.inference_log.append(log_message)

    def display_results(self):
        """Display the facts and inference steps."""

        print("\n" + "=" * 50)
        print("INFERENCE RESULTS")
        print("=" * 50)

        print("\nInitial/Derived Facts:")
        for fact in sorted(self.facts):
            print(f"- {fact.replace('_', ' ').title()}")

        print("\nInference Log:")
        if self.inference_log:
            for number, step in enumerate(self.inference_log, start=1):
                print(f"{number}. {step}")
        else:
            print("No rules were triggered.")

        print("\nFinal Conclusions:")
        if self.inference_log:
            # Display facts that were derived by rules
            derived_facts = set()

            for rule in self.rules:
                if rule["then"] in self.facts:
                    derived_facts.add(rule["then"])

            for fact in sorted(derived_facts):
                print(f"- {fact.replace('_', ' ').title()}")
        else:
            print("- No conclusion could be inferred.")


def main():
    print("=" * 50)
    print("RULE-BASED EXPERT SYSTEM")
    print("Syntecxhub AI Internship - Project 2")
    print("=" * 50)

    print("\nEnter the symptoms/facts you have.")
    print("Available facts:")

    available_facts = [
        "fever",
        "cough",
        "body_ache",
        "high_fever",
        "difficulty_breathing"
    ]

    for fact in available_facts:
        print(f"- {fact.replace('_', ' ').title()}")

    system = ExpertSystem()

    print("\nEnter your facts one by one.")
    print("Type 'done' when finished.")

    while True:
        user_input = input("\nEnter a fact: ").strip().lower()

        if user_input == "done":
            break

        if user_input in available_facts:
            system.add_fact(user_input)
            print(f"Fact added: {user_input.replace('_', ' ').title()}")

        else:
            print("Invalid fact. Please choose from the available facts.")

    # Perform forward chaining
    system.forward_chain()

    # Display reasoning and conclusions
    system.display_results()


if __name__ == "__main__":
    main()