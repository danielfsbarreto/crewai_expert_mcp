from clients import CrewAiClient


class CrewaiEnterpriseService:
    def __init__(self):
        self._client = CrewAiClient()

    def call(self, question: str):
        inputs = {"prompt": question}
        kickoff_id = self._client.kickoff(inputs)
        result_json = self._client.status(kickoff_id)
        return result_json
