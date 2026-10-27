"""
Syntecxhub Internship Project 2: Rule-Based Expert System
Description: A modular forward-chaining rule engine that takes user-provided facts 
             (e.g., medical symptoms), applies if-then inference rules, logs execution 
             steps, and outputs derived conclusions.
"""

from typing import List, Set, Tuple, Dict


class Rule:
    def __init__(self, antecedents: Set[str], consequent: str, description: str = ""):
        """
        Represents an IF-THEN rule.
        :param antecedents: Set of required facts (IF condition)
        :param consequent: New fact to infer (THEN result)
        :param description: Friendly description of the rule
        """
        self.antecedents = set(antecedents)
        self.consequent = consequent
        self.description = description

    def matches(self, facts: Set[str]) -> bool:
        """Checks if all prerequisite facts are present in the current knowledge base."""
        return self.antecedents.issubset(facts)


class ExpertSystem:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.knowledge_base: Set[str] = set()
        self.inference_log: List[str] = []

    def reset(self):
        """Clears current knowledge base and log."""
        self.knowledge_base.clear()
        self.inference_log.clear()

    def add_initial_facts(self, facts: List[str]):
        """Adds initial user-supplied facts to the knowledge base."""
        for fact in facts:
            clean_fact = fact.strip().lower()
            if clean_fact:
                self.knowledge_base.add(clean_fact)

    def run_forward_chaining(self) -> Tuple[Set[str], List[str]]:
        """
        Executes multi-step forward chaining inference until no new facts can be derived.
        Returns the final knowledge base and step-by-step logs.
        """
        self.inference_log.append("--- Starting Inference Engine (Forward Chaining) ---")
        self.inference_log.append(f"Initial Facts: {sorted(list(self.knowledge_base))}")
        
        fired_rules = set()
        changed = True
        step = 1

        while changed:
            changed = False
            for idx, rule in enumerate(self.rules):
                # Check if rule hasn't fired yet and its conditions are met
                if idx not in fired_rules and rule.matches(self.knowledge_base):
                    # If the conclusion is already in knowledge base, skip
                    if rule.consequent in self.knowledge_base:
                        fired_rules.add(idx)
                        continue

                    # Infer new fact
                    self.knowledge_base.add(rule.consequent)
                    fired_rules.add(idx)
                    changed = True

                    log_entry = (
                        f"Step {step}: Rule [{rule.description or f'R{idx+1}'}] triggered! "
                        f"IF {sorted(list(rule.antecedents))} THEN derived '{rule.consequent}'"
                    )
                    self.inference_log.append(log_entry)
                    step += 1

        if step == 1:
            self.inference_log.append("No rules triggered based on provided facts.")
        else:
            self.inference_log.append("--- Inference Completed: No further rules can fire ---")

        return self.knowledge_base, self.inference_log


def load_sample_medical_rules() -> List[Rule]:
    """Pre-loads a domain-specific set of rules (Medical Diagnosis Example)."""
    return [
        Rule({"fever", "cough"}, "respiratory_infection", "Detect Respiratory Infection"),
        Rule({"respiratory_infection", "fatigue"}, "flu", "Diagnose Flu"),
        Rule({"respiratory_infection", "shortness_of_breath"}, "severe_respiratory_issue", "Diagnose Severe Issue"),
        Rule({"severe_respiratory_issue", "chest_pain"}, "pneumonia_risk", "High Risk Pneumonia"),
        Rule({"fever", "rash"}, "viral_exanthem", "Diagnose Viral Exanthem"),
        Rule({"headache", "stiff_neck", "fever"}, "meningitis_risk", "High Risk Meningitis"),
        Rule({"flu"}, "recommend_rest_and_fluids", "Treatment Recommendation"),
        Rule({"pneumonia_risk"}, "recommend_emergency_care", "Urgent Care Recommendation"),
    ]


def interactive_cli():
    """Runs interactive Command-Line Interface."""
    print("=" * 60)
    print("       WELCOME TO THE RULE-BASED EXPERT SYSTEM")
    print("=" * 60)

    rules = load_sample_medical_rules()
    system = ExpertSystem(rules)

    print("\nAvailable Pre-defined Symptoms/Facts for Testing:")
    available_facts = [
        "fever", "cough", "fatigue", "shortness_of_breath", 
        "chest_pain", "rash", "stiff_neck", "headache"
    ]
    print(", ".join(available_facts))
    print("-" * 60)

    user_input = input("\nEnter initial symptoms/facts (comma-separated): ")
    initial_facts = [f.strip() for f in user_input.split(",")]

    system.reset()
    system.add_initial_facts(initial_facts)
    final_kb, logs = system.run_forward_chaining()

    print("\n" + "=" * 60)
    print("                 INFERENCE LOGS")
    print("=" * 60)
    for log in logs:
        print(log)

    print("\n" + "=" * 60)
    print("              FINAL KNOWLEDGE BASE")
    print("=" * 60)
    for fact in sorted(list(final_kb)):
        print(f" - {fact}")
    print("=" * 60)


if __name__ == "__main__":
    interactive_cli()