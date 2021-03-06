# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/moluscedialogbase.ui'
#
# Created: Wed Mar 20 10:55:43 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(660, 382)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabInputs = QtGui.QWidget()
        self.tabInputs.setObjectName(_fromUtf8("tabInputs"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabInputs)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.tabInputs)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.lstLayers = QtGui.QListWidget(self.splitter)
        self.lstLayers.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lstLayers.setAlternatingRowColors(True)
        self.lstLayers.setObjectName(_fromUtf8("lstLayers"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnSetInitialRaster = QtGui.QPushButton(self.widget)
        self.btnSetInitialRaster.setObjectName(_fromUtf8("btnSetInitialRaster"))
        self.gridLayout_2.addWidget(self.btnSetInitialRaster, 0, 0, 1, 1)
        self.leInitRasterName = QtGui.QLineEdit(self.widget)
        self.leInitRasterName.setObjectName(_fromUtf8("leInitRasterName"))
        self.gridLayout_2.addWidget(self.leInitRasterName, 0, 1, 1, 1)
        self.btnSetFinalRaster = QtGui.QPushButton(self.widget)
        self.btnSetFinalRaster.setObjectName(_fromUtf8("btnSetFinalRaster"))
        self.gridLayout_2.addWidget(self.btnSetFinalRaster, 1, 0, 1, 1)
        self.leInitYear = QtGui.QLineEdit(self.widget)
        self.leInitYear.setObjectName(_fromUtf8("leInitYear"))
        self.gridLayout_2.addWidget(self.leInitYear, 0, 2, 1, 1)
        self.leFinalRasterName = QtGui.QLineEdit(self.widget)
        self.leFinalRasterName.setObjectName(_fromUtf8("leFinalRasterName"))
        self.gridLayout_2.addWidget(self.leFinalRasterName, 1, 1, 1, 1)
        self.leFinalYear = QtGui.QLineEdit(self.widget)
        self.leFinalYear.setObjectName(_fromUtf8("leFinalYear"))
        self.gridLayout_2.addWidget(self.leFinalYear, 1, 2, 1, 1)
        self.lstFactors = QtGui.QListWidget(self.widget)
        self.lstFactors.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lstFactors.setAlternatingRowColors(True)
        self.lstFactors.setObjectName(_fromUtf8("lstFactors"))
        self.gridLayout_2.addWidget(self.lstFactors, 4, 1, 5, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.btnRemoveAllFactors = QtGui.QPushButton(self.widget)
        self.btnRemoveAllFactors.setObjectName(_fromUtf8("btnRemoveAllFactors"))
        self.gridLayout_2.addWidget(self.btnRemoveAllFactors, 8, 0, 1, 1)
        self.btnRemoveFactor = QtGui.QPushButton(self.widget)
        self.btnRemoveFactor.setObjectName(_fromUtf8("btnRemoveFactor"))
        self.gridLayout_2.addWidget(self.btnRemoveFactor, 7, 0, 1, 1)
        self.btnAddFactor = QtGui.QPushButton(self.widget)
        self.btnAddFactor.setObjectName(_fromUtf8("btnAddFactor"))
        self.gridLayout_2.addWidget(self.btnAddFactor, 6, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.splitter)
        self.tabWidget.addTab(self.tabInputs, _fromUtf8(""))
        self.tabAreaChanges = QtGui.QWidget()
        self.tabAreaChanges.setObjectName(_fromUtf8("tabAreaChanges"))
        self.gridLayout = QtGui.QGridLayout(self.tabAreaChanges)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.tabAreaChanges)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tabAreaChanges)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.btnUpdateStatistics = QtGui.QPushButton(self.tabAreaChanges)
        self.btnUpdateStatistics.setObjectName(_fromUtf8("btnUpdateStatistics"))
        self.gridLayout.addWidget(self.btnUpdateStatistics, 4, 0, 1, 1)
        self.btnCreateChangeMap = QtGui.QPushButton(self.tabAreaChanges)
        self.btnCreateChangeMap.setObjectName(_fromUtf8("btnCreateChangeMap"))
        self.gridLayout.addWidget(self.btnCreateChangeMap, 4, 1, 1, 1)
        self.tblStatistics = MolusceTableWidget(self.tabAreaChanges)
        self.tblStatistics.setObjectName(_fromUtf8("tblStatistics"))
        self.tblStatistics.setColumnCount(0)
        self.tblStatistics.setRowCount(0)
        self.gridLayout.addWidget(self.tblStatistics, 1, 0, 1, 2)
        self.tblTransMatrix = MolusceTableWidget(self.tabAreaChanges)
        self.tblTransMatrix.setObjectName(_fromUtf8("tblTransMatrix"))
        self.tblTransMatrix.setColumnCount(0)
        self.tblTransMatrix.setRowCount(0)
        self.gridLayout.addWidget(self.tblTransMatrix, 3, 0, 1, 2)
        self.tabWidget.addTab(self.tabAreaChanges, _fromUtf8(""))
        self.tabModel = QtGui.QWidget()
        self.tabModel.setObjectName(_fromUtf8("tabModel"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabModel)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.grpSampling = QgsCollapsibleGroupBox(self.tabModel)
        self.grpSampling.setCheckable(True)
        self.grpSampling.setChecked(False)
        self.grpSampling.setProperty("collapsed", True)
        self.grpSampling.setProperty("saveCollapsedState", True)
        self.grpSampling.setProperty("saveCheckedState", True)
        self.grpSampling.setObjectName(_fromUtf8("grpSampling"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.grpSampling)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.grpSampling)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.cmbSamplingMode = QtGui.QComboBox(self.grpSampling)
        self.cmbSamplingMode.setObjectName(_fromUtf8("cmbSamplingMode"))
        self.horizontalLayout.addWidget(self.cmbSamplingMode)
        self.label_6 = QtGui.QLabel(self.grpSampling)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.spnSamplesCount = QtGui.QSpinBox(self.grpSampling)
        self.spnSamplesCount.setMaximum(100000000)
        self.spnSamplesCount.setProperty("value", 1000)
        self.spnSamplesCount.setObjectName(_fromUtf8("spnSamplesCount"))
        self.horizontalLayout.addWidget(self.spnSamplesCount)
        self.gridLayout_3.addWidget(self.grpSampling, 0, 0, 1, 3)
        self.label_4 = QtGui.QLabel(self.tabModel)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.cmbSimulationMethod = QtGui.QComboBox(self.tabModel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbSimulationMethod.sizePolicy().hasHeightForWidth())
        self.cmbSimulationMethod.setSizePolicy(sizePolicy)
        self.cmbSimulationMethod.setObjectName(_fromUtf8("cmbSimulationMethod"))
        self.gridLayout_3.addWidget(self.cmbSimulationMethod, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        self.widgetStackMethods = QtGui.QStackedWidget(self.tabModel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetStackMethods.sizePolicy().hasHeightForWidth())
        self.widgetStackMethods.setSizePolicy(sizePolicy)
        self.widgetStackMethods.setFrameShape(QtGui.QFrame.NoFrame)
        self.widgetStackMethods.setFrameShadow(QtGui.QFrame.Sunken)
        self.widgetStackMethods.setObjectName(_fromUtf8("widgetStackMethods"))
        self.gridLayout_3.addWidget(self.widgetStackMethods, 2, 0, 1, 3)
        self.tabWidget.addTab(self.tabModel, _fromUtf8(""))
        self.tabSimulation = QtGui.QWidget()
        self.tabSimulation.setObjectName(_fromUtf8("tabSimulation"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tabSimulation)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.btnSelectRiskFunction = QtGui.QPushButton(self.tabSimulation)
        self.btnSelectRiskFunction.setEnabled(False)
        self.btnSelectRiskFunction.setObjectName(_fromUtf8("btnSelectRiskFunction"))
        self.gridLayout_4.addWidget(self.btnSelectRiskFunction, 0, 2, 1, 1)
        self.leRiskValidationPath = QtGui.QLineEdit(self.tabSimulation)
        self.leRiskValidationPath.setEnabled(False)
        self.leRiskValidationPath.setObjectName(_fromUtf8("leRiskValidationPath"))
        self.gridLayout_4.addWidget(self.leRiskValidationPath, 1, 1, 1, 1)
        self.btnSelectRiskValidation = QtGui.QPushButton(self.tabSimulation)
        self.btnSelectRiskValidation.setEnabled(False)
        self.btnSelectRiskValidation.setObjectName(_fromUtf8("btnSelectRiskValidation"))
        self.gridLayout_4.addWidget(self.btnSelectRiskValidation, 1, 2, 1, 1)
        self.chkRiskFunction = QtGui.QCheckBox(self.tabSimulation)
        self.chkRiskFunction.setObjectName(_fromUtf8("chkRiskFunction"))
        self.gridLayout_4.addWidget(self.chkRiskFunction, 0, 0, 1, 1)
        self.leRiskFunctionPath = QtGui.QLineEdit(self.tabSimulation)
        self.leRiskFunctionPath.setEnabled(False)
        self.leRiskFunctionPath.setObjectName(_fromUtf8("leRiskFunctionPath"))
        self.gridLayout_4.addWidget(self.leRiskFunctionPath, 0, 1, 1, 1)
        self.chkRiskValidation = QtGui.QCheckBox(self.tabSimulation)
        self.chkRiskValidation.setObjectName(_fromUtf8("chkRiskValidation"))
        self.gridLayout_4.addWidget(self.chkRiskValidation, 1, 0, 1, 1)
        self.chkMonteCarlo = QtGui.QCheckBox(self.tabSimulation)
        self.chkMonteCarlo.setObjectName(_fromUtf8("chkMonteCarlo"))
        self.gridLayout_4.addWidget(self.chkMonteCarlo, 2, 0, 1, 1)
        self.leMonteCarloPath = QtGui.QLineEdit(self.tabSimulation)
        self.leMonteCarloPath.setEnabled(False)
        self.leMonteCarloPath.setObjectName(_fromUtf8("leMonteCarloPath"))
        self.gridLayout_4.addWidget(self.leMonteCarloPath, 2, 1, 1, 1)
        self.btnSelectMonteCarlo = QtGui.QPushButton(self.tabSimulation)
        self.btnSelectMonteCarlo.setEnabled(False)
        self.btnSelectMonteCarlo.setObjectName(_fromUtf8("btnSelectMonteCarlo"))
        self.gridLayout_4.addWidget(self.btnSelectMonteCarlo, 2, 2, 1, 1)
        self.chkReuseMatrix = QtGui.QCheckBox(self.tabSimulation)
        self.chkReuseMatrix.setObjectName(_fromUtf8("chkReuseMatrix"))
        self.gridLayout_4.addWidget(self.chkReuseMatrix, 4, 0, 1, 1)
        self.leMatrixPath = QtGui.QLineEdit(self.tabSimulation)
        self.leMatrixPath.setEnabled(False)
        self.leMatrixPath.setObjectName(_fromUtf8("leMatrixPath"))
        self.gridLayout_4.addWidget(self.leMatrixPath, 4, 1, 1, 1)
        self.btnSelectMatrix = QtGui.QPushButton(self.tabSimulation)
        self.btnSelectMatrix.setEnabled(False)
        self.btnSelectMatrix.setObjectName(_fromUtf8("btnSelectMatrix"))
        self.gridLayout_4.addWidget(self.btnSelectMatrix, 4, 2, 1, 1)
        self.lblIterations = QtGui.QLabel(self.tabSimulation)
        self.lblIterations.setEnabled(False)
        self.lblIterations.setObjectName(_fromUtf8("lblIterations"))
        self.gridLayout_4.addWidget(self.lblIterations, 3, 1, 1, 1)
        self.spnIterations = QtGui.QSpinBox(self.tabSimulation)
        self.spnIterations.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnIterations.sizePolicy().hasHeightForWidth())
        self.spnIterations.setSizePolicy(sizePolicy)
        self.spnIterations.setMinimum(1)
        self.spnIterations.setMaximum(100)
        self.spnIterations.setProperty("value", 1)
        self.spnIterations.setObjectName(_fromUtf8("spnIterations"))
        self.gridLayout_4.addWidget(self.spnIterations, 3, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(20, 94, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 1, 0, 1, 1)
        self.btnStartSimulation = QtGui.QPushButton(self.tabSimulation)
        self.btnStartSimulation.setObjectName(_fromUtf8("btnStartSimulation"))
        self.gridLayout_5.addWidget(self.btnStartSimulation, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabSimulation, _fromUtf8(""))
        self.tabMessages = QtGui.QWidget()
        self.tabMessages.setObjectName(_fromUtf8("tabMessages"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabMessages)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.txtMessages = QtGui.QTextEdit(self.tabMessages)
        self.txtMessages.setUndoRedoEnabled(False)
        self.txtMessages.setReadOnly(True)
        self.txtMessages.setObjectName(_fromUtf8("txtMessages"))
        self.verticalLayout_4.addWidget(self.txtMessages)
        self.tabWidget.addTab(self.tabMessages, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.widgetStackMethods.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "MOLUSCE", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSetInitialRaster.setText(QtGui.QApplication.translate("Dialog", "Initial >>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSetFinalRaster.setText(QtGui.QApplication.translate("Dialog", "Final >>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemoveAllFactors.setText(QtGui.QApplication.translate("Dialog", "<< Remove all", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemoveFactor.setText(QtGui.QApplication.translate("Dialog", "<< Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddFactor.setText(QtGui.QApplication.translate("Dialog", "Add >>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Factors driving landuse changes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInputs), QtGui.QApplication.translate("Dialog", "Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Class statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Transition matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUpdateStatistics.setText(QtGui.QApplication.translate("Dialog", "Update tables", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCreateChangeMap.setText(QtGui.QApplication.translate("Dialog", "Create changes map", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAreaChanges), QtGui.QApplication.translate("Dialog", "Area Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.grpSampling.setTitle(QtGui.QApplication.translate("Dialog", "Define Samples", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Number of samples", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Method", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabModel), QtGui.QApplication.translate("Dialog", "Samples and Model", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectRiskFunction.setText(QtGui.QApplication.translate("Dialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectRiskValidation.setText(QtGui.QApplication.translate("Dialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.chkRiskFunction.setText(QtGui.QApplication.translate("Dialog", "Risk function", None, QtGui.QApplication.UnicodeUTF8))
        self.chkRiskValidation.setText(QtGui.QApplication.translate("Dialog", "Risk class validation", None, QtGui.QApplication.UnicodeUTF8))
        self.chkMonteCarlo.setText(QtGui.QApplication.translate("Dialog", "Monte Carlo simulations", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectMonteCarlo.setText(QtGui.QApplication.translate("Dialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.chkReuseMatrix.setText(QtGui.QApplication.translate("Dialog", "Reuse input matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectMatrix.setText(QtGui.QApplication.translate("Dialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.lblIterations.setText(QtGui.QApplication.translate("Dialog", "Number of simulation iterations", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStartSimulation.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSimulation), QtGui.QApplication.translate("Dialog", "Risk Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMessages), QtGui.QApplication.translate("Dialog", "Messages", None, QtGui.QApplication.UnicodeUTF8))

from qgis.gui import QgsCollapsibleGroupBox
from molusce.moluscetablewidget import MolusceTableWidget
