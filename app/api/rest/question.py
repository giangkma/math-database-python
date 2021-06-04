from flask.views import MethodView
from flask_smorest import Blueprint
from flask_smorest.pagination import PaginationParameters
from flask import jsonify, make_response

from app.api.business.question import findQuestionById
from app.api.schema.question import QuestionQuerySchema, QuestionSchema, UpdateQuestionSchema, CheckAnswerQuestionSchema
from app.cache import cache
from app.model.question import Questions

api = Blueprint(
    "Questions API",
    __name__,
    url_prefix="/api/v1/questions",
    description="In this API you can create, search or update questions.",
)


@api.route("")
class QuestionsAPI(MethodView):
    @classmethod
    @api.arguments(QuestionQuerySchema, location="query")
    @api.paginate()
    @api.response(200, QuestionSchema(many=True))
    def get(cls, recipe_args: dict, pagination_parameters: PaginationParameters):
        """List questions"""
        result = Questions.objects(
            **recipe_args).paginate(pagination_parameters.page, pagination_parameters.page_size)
        pagination_parameters.item_count = result.total
        return result.items

    @classmethod
    @api.arguments(QuestionSchema)
    @api.response(201, QuestionSchema)
    def post(cls, question_data: dict):
        """Add a new question"""
        item = Questions(**question_data)
        item.save()
        return item


@api.route("/<question_id>")
class QuestionAPI(MethodView):
    @classmethod
    @api.response(200, QuestionSchema)
    @cache.memoize(timeout=30)
    def get(cls, question_id: str):
        """Get question by ID"""
        return findQuestionById(question_id).first()

    @classmethod
    @api.arguments(UpdateQuestionSchema)
    @api.response(200, QuestionSchema)
    def put(cls, question_data: dict, question_id: str):
        """Update existing question"""
        if not question_data:
            return findQuestionById(question_id).first()
        item = findQuestionById(question_id).first()
        item.update(**question_data)
        item.save()
        return findQuestionById(question_id).first()

    @classmethod
    @api.response(200)
    def delete(cls, question_id: str):
        """Delete question"""
        findQuestionById(question_id).delete()

    @classmethod
    @api.arguments(CheckAnswerQuestionSchema)
    @api.response(200)
    def post(cls, data: dict, question_id: str):
        """Check answer of question"""
        item = findQuestionById(question_id).first()
        if item["correctAnswer"] == data["answer"]:
            return make_response(jsonify({
                "correct": True
            }))
        return make_response(jsonify({
            "correct": False
        }))
