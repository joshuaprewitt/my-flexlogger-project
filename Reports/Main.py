# -----------------------------------------------------------------------------
# -- Main Python script for Analysis Automation
# -- Created: 8/11/2020 3:06:08 PM
# -- Author:  Josh Prewitt
# -- Package: My FlexLogger Python Report
# -- Comment:  Main file with entry points for Analysis Automation
# -----------------------------------------------------------------------------
# ! python
import DIAdem  # Enable access to DIAdem commands and variables
import os


# -----------------------------------------------------------------------------
# \brief Routine for initializing parallel processing.
#        This routine is only called when the evaluation mode is set
#        to "Parallel". In this case this routine is called once before
#        processing all data.
#
# \param oContext [In/Out]:  Object which transfers parameters from the server
#                            to the routine and vice versa.
# -----------------------------------------------------------------------------
def On_Initialize(oContext):

    dd = DIAdem.Application
    dd.ApplicationSetLocale("english")

#   Please enter your code sequences here.
#   --------------------------------------

    oContext.LogResult("On_Initialize: Initialization complete")

# end of On_Initialize() --------------------------
# -------------------------------------------------


# -----------------------------------------------------------------------------
# \brief This is the analysis method which is called by Analysis Server.
#      The routine is called to analyze a "DataLink"
#
#      For the "Parallel" evaluation mode, the routine is called several times
#      (depending on the DataLink).
#      For the "Comparative Evaluation" the routine is called once with all
#      DataLinks.
#
# \param oContext [In/Out]:  Object which transfers parameters from the server
#                            to the routine and back.
# -----------------------------------------------------------------------------
def On_Run_AnalysisProcedure(oContext):

    dd = DIAdem.Application
    dd.ApplicationSetLocale("english")

#    Please enter your code sequences here.
#    --------------------------------------

    for link in oContext.DataLinks:
        elements = dd.Navigator.LoadData(link)
        oContext.LogWarning("Loaded elements: "+str(elements.Count))
        break
    
    ResultsPath = oContext.Procedure.Arguments("ResultsPath").Value   
    oContext.LogResult("Results Path = "+str(ResultsPath))
    
    dd.Report.LoadLayout(dd.CurrentScriptPath+"FlexLogger.TDR")
    dd.Report.Refresh()
    #oContext.LogResult(dd.CurrentScriptPath+"FlexLogger.TDR")
    
    file_name = os.path.splitext(dd.Data.Root.ChannelGroups(2).Channels(1).Properties("sourcedatafilename").Value)[0]+".pdf"
    oContext.LogResult("file_name = "+file_name)
    
    pdfExportPath = ResultsPath+"\\"+file_name
    dd.Report.Sheets.ExportToPDF(pdfExportPath,False)
    
    oContext.FileService.UploadResultFile(pdfExportPath, "", "Documents", False)

    oContext.LogResult("On_Run_AnalysisProcedure: End of Analysis procedure")

# end of On_Run_AnalysisProcedure() -------------------
# -----------------------------------------------------


# -----------------------------------------------------------------------------
# \brief Routine to complete parallel processing.
#        This routine is only called when the evaluation mode is set
#        to "Parallel". In this case this routine is called once after
#        all data has been processed.
#
# \param oContext [In/Out]:  Object for the transfer of parameters from
#                            the server to the routine and vice versa.
# -----------------------------------------------------------------------------
def On_Finalize(oContext):

    dd = DIAdem.Application
    dd.ApplicationSetLocale("english")

#    Please enter your code sequences here.
#    --------------------------------------

    oContext.LogResult("On_Finalize: Closing sequence complete")

# end of On_Finalize() --------------------------------
# -----------------------------------------------------
