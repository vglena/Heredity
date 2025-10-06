
import csv
import itertools
import sys

PROBS = {
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },
    "trait": {
        2: {True: 0.65, False: 0.35},
        1: {True: 0.56, False: 0.44},
        0: {True: 0.01, False: 0.99}
    },
    "mutation": 0.01
}


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    
    people = load_data(sys.argv[1])
    if not people:
        sys.exit("No people found in CSV or CSV is invalid.")

    probabilities = {
        person: {
            "gene": {2: 0, 1: 0, 0: 0},
            "trait": {True: 0, False: 0}
        } for person in people
    }

    # Optional debug: show loaded people
    # print("Loaded people:", people)

    names = set(people)
    for have_trait in powerset(names):
        # Skip sets that contradict known traits
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                print(f"    {value}: {probabilities[person][field][value]:.4f}")


def load_data(filename):
    """Load gene and trait data from a CSV file, stripping whitespace."""
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"].strip()
            mother = row["mother"].strip() or None
            father = row["father"].strip() or None
            trait_val = row["trait"].strip() if row["trait"] else ""
            if trait_val == "1":
                trait = True
            elif trait_val == "0":
                trait = False
            else:
                trait = None

            data[name] = {
                "name": name,
                "mother": mother,
                "father": father,
                "trait": trait
            }
    return data


def powerset(s):
    """Return a list of all possible subsets of set s."""
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s)+1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    probability = 1
    for person in people:
        if person in two_genes:
            genes = 2
        elif person in one_gene:
            genes = 1
        else:
            genes = 0

        has_trait = person in have_trait
        mother = people[person]["mother"]
        father = people[person]["father"]

        if mother is None and father is None:
            gene_prob = PROBS["gene"][genes]
        else:
            def pass_prob(parent):
                if parent in two_genes:
                    return 1 - PROBS["mutation"]
                elif parent in one_gene:
                    return 0.5
                else:
                    return PROBS["mutation"]

            mom_pass = pass_prob(mother)
            dad_pass = pass_prob(father)

            if genes == 2:
                gene_prob = mom_pass * dad_pass
            elif genes == 1:
                gene_prob = mom_pass * (1 - dad_pass) + (1 - mom_pass) * dad_pass
            else:
                gene_prob = (1 - mom_pass) * (1 - dad_pass)

        trait_prob = PROBS["trait"][genes][has_trait]
        probability *= gene_prob * trait_prob

    return probability


def update(probabilities, one_gene, two_genes, have_trait, p):
    """Add joint probability p to the appropriate entries."""
    for person in probabilities:
        if person in two_genes:
            genes = 2
        elif person in one_gene:
            genes = 1
        else:
            genes = 0

        has_trait = person in have_trait
        probabilities[person]["gene"][genes] += p
        probabilities[person]["trait"][has_trait] += p


def normalize(probabilities):
    """Normalize each distribution so that values sum to 1."""
    for person in probabilities:
        total_gene = sum(probabilities[person]["gene"].values())
        for g in probabilities[person]["gene"]:
            probabilities[person]["gene"][g] /= total_gene

        total_trait = sum(probabilities[person]["trait"].values())
        for t in probabilities[person]["trait"]:
            probabilities[person]["trait"][t] /= total_trait


if __name__ == "__main__":
    main()



