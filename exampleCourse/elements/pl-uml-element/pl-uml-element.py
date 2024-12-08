def render(element_html, data):
    return """

    <div class="p-2 w-full h-full flex flex-col gap-0">
        <div>
Design an Entity Relationship Diagram (ERD) with the following requirements: Entities and Attributes: 1. Student, with attributes: Student_ID (PK) and Name. 2. Course, with attributes: Course_ID (PK) and Course_Name. Relationship: A Student enrolls in a Course (many-to-many relationship). Your ERD should include the two entities, their attributes, and the relationship between them. Use appropriate notation to show the many-to-many cardinality.
        </div>
        <div class="flex flex-row gap-2 w-full h-full border-stone-500">
            <div class="p-2 border basis-36 overflow-x-scroll no-scrollbar flex flex-col content-center">
                <p class="font-bold text-center">Toolbox</p>
                <div id="toolbox" class="flex flex-row justify-center flex-wrap gap-2 mt-2">
                </div>
            </div>
            <div style="height: 300px;" class="flex flex-col h-full flex-1 border overflow-hidden">
                <div id="graph-container" class="h-full w-full touch-pan-x touch-pan-y"></div>
            </div>
            <div class="p-2 border">
                <p class="font-bold text-center mb-2">Properties</p>
                <div id="properties-manager" autocomplete="off" autocapitalize="off"/>
            </div>
        </div>
    </div>
    """


def grade(element_html, data):
    pass
