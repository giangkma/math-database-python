from app.api.business.common import findById
from app.api.exceptions.question import QuestionNotFound
from app.model.question import Questions


def findQuestionById(id: str) -> Questions:
    return findById(Questions, id, QuestionNotFound)
