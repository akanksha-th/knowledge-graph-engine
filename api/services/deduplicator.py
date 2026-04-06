from api.schema.graph import KnowledgeGraph, Triple


class DeduplicationService:
    @staticmethod
    def deduplicate_triples(kg: KnowledgeGraph) -> list[Triple]:
        seen = set()
        unique_triples = []
        for triple in kg.triples:
            triple_tuple = (
                triple.subject.lower(),
                triple.predicate.lower(),
                triple.obj.lower(),
            )
            if triple_tuple not in seen:
                seen.add(triple_tuple)
                unique_triples.append(triple)
        return unique_triples