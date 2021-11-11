from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from pybo.models import Question
from werkzeug.utils import redirect
from .. import db
from ..models import Question
from ..forms import QuestionForm

NAME = 'question'
bp = Blueprint(NAME, __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', 
                            question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',
                            question=question)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index')) # POST 방식 요청이면 데이터 저장 후 질문 목록 페이지로 이동
    return render_template('question/question_form.html', form=form) # GET 방식 요청이면 질문 등록 페이지 렌더링
