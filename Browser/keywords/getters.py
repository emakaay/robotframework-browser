from typing import Any

from robot.api import logger  # type: ignore
from robotlibcore import keyword  # type: ignore

from ..generated import playwright_pb2
from ..assertion_engine import verify_assertion, AssertionOperator


class Getters:
    def __init__(self, library):
        self.library = library

    @property
    def playwright(self):
        return self.library.playwright

    @keyword
    def get_url(
        self,
        assertion_operator=AssertionOperator.NO_ASSERTION,
        assertion_value: Any = None,
    ) -> str:
        """ Returns current URL.

            Optionally asserts that it matches the specified assertion.
        """
        value = ""
        with self.playwright.grpc_channel() as stub:
            response = stub.GetUrl(playwright_pb2.Empty())
            logger.info(response.log)
            value = response.body
        verify_assertion(value, assertion_operator, assertion_value, "URL ")
        return value

    @keyword
    def get_title(
        self,
        assertion_operator=AssertionOperator.NO_ASSERTION,
        assertion_value: Any = None,
    ):
        """ Returns current page Title.

            Optionally asserts that it matches the specified assertion.
        """
        value = None
        with self.playwright.grpc_channel() as stub:
            response = stub.GetTitle(playwright_pb2.Empty())
            logger.info(response.log)
            value = response.body
        verify_assertion(value, assertion_operator, assertion_value, "Title ")
        return value

    @keyword
    def get_text(
        self,
        selector: str,
        assertion_operator=AssertionOperator.NO_ASSERTION,
        assertion_value: Any = None,
    ):
        """ Returns element's text attribute.

            Optionally asserts that it matches the specified assertion.
        """
        value = None
        with self.playwright.grpc_channel() as stub:
            response = stub.GetDomProperty(
                playwright_pb2.getDomPropertyRequest(
                    selector=selector, property="innerText"
                )
            )
            logger.info(response.log)
            value = response.body
        verify_assertion(value, assertion_operator, assertion_value, f"Text {selector}")
        return value

    @keyword
    def get_attribute(
        self,
        selector: str,
        attribute: str,
        assertion_operator=AssertionOperator.NO_ASSERTION,
        assertion_value: Any = None,
    ):
        """ Returns specified attribute.

            Optionally asserts that it matches the specified assertion.
        """
        with self.playwright.grpc_channel() as stub:
            response = stub.GetDomProperty(
                playwright_pb2.getDomPropertyRequest(
                    selector=selector, property=attribute
                )
            )
            logger.info(response.log)
            value = response.body
        verify_assertion(
            value, assertion_operator, assertion_value, f"Attribute {selector}"
        )
        return value

    @keyword
    def get_textfield_value(
        self,
        selector: str,
        assertion_operator=AssertionOperator.NO_ASSERTION,
        assertion_value: Any = None,
    ):
        """ Returns textfieds value.

            Optionally asserts that it matches the specified assertion.
        """
        value = None
        with self.playwright.grpc_channel() as stub:
            response = stub.GetDomProperty(
                playwright_pb2.getDomPropertyRequest(
                    selector=selector, property="value"
                )
            )
            logger.info(response.log)
            value = response.body
        verify_assertion(
            value, assertion_operator, assertion_value, f"Element {selector} value "
        )
        return value
